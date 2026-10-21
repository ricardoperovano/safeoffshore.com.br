"""Gera as galerias de fotos do site a partir de content/galerias/*.json.

Os arquivos JSON são editados pelo painel (Pages CMS, ver .pages.yml). Para cada
galeria, este script:
  1. otimiza as fotos (redimensiona, gera .jpg/.png + .webp) em images/galerias/<galeria>/;
  2. reescreve o HTML entre os marcadores <!-- galeria:<nome> --> e <!-- /galeria:<nome> -->
     nas páginas configuradas em GALERIAS.

Páginas em /en/ usam os campos com sufixo "_en" (titulo_en, descricao_en, legenda_en,
local_en); se estiverem vazios, usam o texto em português.

Uso: python scripts/galerias.py   (requer Pillow)
"""
import hashlib
import html
import json
import re
import sys
import unicodedata
from pathlib import Path

from PIL import Image, ImageOps

RAIZ = Path(__file__).resolve().parent.parent
SAIDA = RAIZ / "images" / "galerias"
MANIFESTO = SAIDA / "manifesto.json"

# modelo -> como a galeria é desenhada; paginas -> (arquivo, variante)
GALERIAS = {
    "hidreletricas": {"rotulo": "Hidrelétricas", "modelo": "grade", "paginas": [("servicos/hidreletricas/index.html", None), ("en/services/hydropower-plants/index.html", None)]},
    "apoio-subaquatico": {"rotulo": "Apoio Subaquático", "modelo": "grade", "paginas": [("servicos/apoio-subaquatico/index.html", None), ("en/services/underwater-services/index.html", None)]},
    "reparo-naval": {"rotulo": "Reparo Naval", "modelo": "grade", "paginas": [("servicos/reparo-naval/index.html", None), ("en/services/underwater-ship-repair/index.html", None)]},
    "obras-civis": {"rotulo": "Obras Civis", "modelo": "grade", "paginas": [("servicos/obras-civis/index.html", None), ("en/services/underwater-civil-works/index.html", None)]},
    "documentacao-marinha": {"rotulo": "Documentação Marinha", "modelo": "grade", "paginas": [("servicos/documentacao-marinha/index.html", None), ("en/services/brazilian-navy-permits/index.html", None)]},
    "agulha-magnetica": {"rotulo": "Agulha Magnética", "modelo": "grade", "paginas": [("servicos/agulha-magnetica-e-barometro-aneroide/index.html", None), ("en/services/magnetic-compass-adjustment/index.html", None)]},
    "defensas-portos": {"rotulo": "Defensas de Portos", "modelo": "grade", "paginas": [("servicos/defensas-portos/index.html", None), ("en/services/port-fenders/index.html", None)]},
    "sinalizacao-nautica": {"rotulo": "Sinalização Náutica", "modelo": "legendas", "paginas": [("servicos/sinalizacao-nautica/index.html", None), ("en/services/aids-to-navigation/index.html", None)]},
    "projetos": {"rotulo": "Projetos Realizados", "modelo": "projetos", "paginas": [("index.html", None), ("en/index.html", None)]},
    "clientes": {"rotulo": "Clientes", "modelo": "clientes", "paginas": [("principais-clientes-1/index.html", "pagina"), ("index.html", "home"), ("en/clients/index.html", "pagina"), ("en/index.html", "home")]},
}

LARGURA_MAXIMA = {"grade": 1600, "legendas": 1600, "projetos": 1600, "clientes": 400}
CLIENTES_NA_HOME = 6


def slug(texto):
    texto = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", texto.lower()).strip("-") or "foto"


def tem_transparencia(imagem):
    """True só se a imagem usa transparência de fato (PNG com alfa todo opaco vira JPG)."""
    if imagem.mode == "P":
        return "transparency" in imagem.info
    if imagem.mode in ("RGBA", "LA"):
        return imagem.getchannel("A").getextrema()[0] < 255
    return False


def otimizar(origem, galeria, largura, manifesto, usados):
    """Gera as versões otimizadas da foto e devolve (src, webp, largura, altura) relativos à raiz."""
    hash_origem = hashlib.sha1(origem.read_bytes()).hexdigest()
    pasta = SAIDA / galeria
    pasta.mkdir(parents=True, exist_ok=True)
    with Image.open(origem) as imagem:
        transparente = tem_transparencia(imagem)
    extensao = ".png" if transparente else ".jpg"
    base = slug(origem.stem)
    if base.startswith(galeria + "-"):  # uploads/<galeria>-foto.jpg -> images/galerias/<galeria>/foto.jpg
        base = base[len(galeria) + 1:]
    nome = base
    contador = 2
    while (pasta / (nome + extensao)).relative_to(RAIZ).as_posix() in usados:
        nome = f"{base}-{contador}"
        contador += 1
    destino = pasta / (nome + extensao)
    destino_webp = pasta / (nome + ".webp")
    chave = destino.relative_to(RAIZ).as_posix()
    usados.update({chave, destino_webp.relative_to(RAIZ).as_posix()})
    registro = manifesto.get(chave)
    if not (registro and registro["origem"] == hash_origem and destino.exists() and destino_webp.exists()):
        with Image.open(origem) as imagem:
            imagem = ImageOps.exif_transpose(imagem)
            imagem.thumbnail((largura, largura * 2))
            if transparente:
                imagem = imagem.convert("RGBA")
                imagem.save(destino, optimize=True)
            else:
                imagem = imagem.convert("RGB")
                imagem.save(destino, quality=82, optimize=True, progressive=True)
            imagem.save(destino_webp, quality=80, method=6)
            registro = {"origem": hash_origem, "largura": imagem.width, "altura": imagem.height}
        manifesto[chave] = registro
    return chave, destino_webp.relative_to(RAIZ).as_posix(), registro["largura"], registro["altura"]


def picture(prefixo, foto, alt, extra=""):
    src, webp, largura, altura = foto
    return (f'<picture><source srcset="{prefixo}{webp}" type="image/webp">'
            f'<img loading="lazy" decoding="async" width="{largura}" height="{altura}" '
            f'src="{prefixo}{src}" alt="{html.escape(alt)}"{extra}></picture>')


def texto(dados, campo, ingles, padrao=""):
    """Campo no idioma da página; em inglês, cai para o português se não houver tradução."""
    if ingles and dados.get(campo + "_en"):
        return dados[campo + "_en"]
    return dados.get(campo, padrao)


def renderizar(modelo, variante, dados, itens, prefixo, rotulo, ingles):
    """Devolve as linhas de HTML (sem indentação base) para a galeria."""
    e = html.escape
    sufixo = "Safe Offshore"
    if not itens:
        return []
    if modelo == "grade":
        titulo = texto(dados, "titulo", ingles, "Nossos Trabalhos")
        linhas = ([f"<h3>{e(titulo)}</h3>"] if titulo else []) + ['<div class="service-images-grid">']
        for item, foto in itens:
            alt = texto(item, "descricao", ingles) or f"{rotulo} - {sufixo}"
            linhas += ['    <div class="service-image-item">', "        " + picture(prefixo, foto, alt), "    </div>"]
        return linhas + ["</div>"]
    if modelo == "legendas":
        linhas = []
        if texto(dados, "titulo", ingles):
            linhas += [f'<h3>{e(texto(dados, "titulo", ingles))}</h3>']
        linhas += ['<div class="service-operations-grid">']
        for item, foto in itens:
            legenda = texto(item, "legenda", ingles)
            linhas += ['    <div class="operation-item">',
                       "        " + picture(prefixo, foto, f"{legenda} - Safe Offshore" if legenda else f"{rotulo} - Safe Offshore")]
            if legenda:
                linhas += [f'        <p class="operation-caption">{e(legenda)}</p>']
            linhas += ["    </div>"]
        return linhas + ["</div>"]
    if modelo == "projetos":
        linhas = ['<div class="portfolio-grid">']
        for item, foto in itens:
            titulo, local = texto(item, "titulo", ingles), texto(item, "local", ingles)
            linhas += ['    <div class="portfolio-item">', "        " + picture(prefixo, foto, titulo or ("Project" if ingles else "Projeto")),
                       '        <div class="portfolio-overlay">', "            <div>",
                       f"                <h3>{e(titulo)}</h3>", f"                <p>{e(local)}</p>",
                       "            </div>", "        </div>", "    </div>"]
        return linhas + ["</div>"]
    if modelo == "clientes":
        classe = "client-logo-box" if variante == "home" else "client-item"
        if variante == "home":
            itens = itens[:CLIENTES_NA_HOME]
        linhas = ['<div class="clients-grid">']
        for item, foto in itens:
            linhas += [f'    <div class="{classe}">', "        " + picture(prefixo, foto, texto(item, "nome", ingles) or "Cliente"), "    </div>"]
        return linhas + ["</div>"]
    raise ValueError(f"modelo desconhecido: {modelo}")


def substituir(pagina, nome, linhas):
    caminho = RAIZ / pagina
    texto = caminho.read_bytes().decode("utf-8")  # read_text() trocaria CRLF por LF
    quebra = "\r\n" if "\r\n" in texto else "\n"
    padrao = re.compile(r"(?P<indent>[ \t]*)<!-- galeria:%s -->.*?<!-- /galeria:%s -->" % (re.escape(nome), re.escape(nome)), re.S)
    achado = padrao.search(texto)
    if not achado:
        sys.exit(f"Marcador da galeria '{nome}' não encontrado em {pagina}")
    indent = achado.group("indent")
    corpo = [f"<!-- galeria:{nome} -->"] + linhas + [f"<!-- /galeria:{nome} -->"]
    bloco = quebra.join((indent + linha) if i else linha for i, linha in enumerate(corpo))
    novo = texto[:achado.start()] + indent + bloco + texto[achado.end():]
    if novo != texto:
        caminho.write_text(novo, encoding="utf-8", newline="")
        return True
    return False


def main():
    manifesto = json.loads(MANIFESTO.read_text(encoding="utf-8")) if MANIFESTO.exists() else {}
    usados = set()
    alteradas = []
    for nome, config in GALERIAS.items():
        dados = json.loads((RAIZ / "content" / "galerias" / f"{nome}.json").read_text(encoding="utf-8"))
        modelo = config["modelo"]
        itens = []
        for item in dados.get("fotos") or []:
            imagem = (item.get("imagem") or "").lstrip("/")
            if not imagem:
                continue
            origem = RAIZ / imagem
            if not origem.exists():
                sys.exit(f"[{nome}] foto não encontrada: {imagem}")
            itens.append((item, otimizar(origem, nome, LARGURA_MAXIMA[modelo], manifesto, usados)))
        for pagina, variante in config["paginas"]:
            prefixo = "../" * pagina.count("/")
            ingles = pagina.startswith("en/")
            if substituir(pagina, nome, renderizar(modelo, variante, dados, itens, prefixo, config["rotulo"], ingles)):
                alteradas.append(pagina)
    # remove versões otimizadas de fotos que saíram das galerias
    for arquivo in SAIDA.rglob("*"):
        if arquivo.is_file() and arquivo != MANIFESTO and arquivo.relative_to(RAIZ).as_posix() not in usados:
            arquivo.unlink()
    for pasta in SAIDA.iterdir():
        if pasta.is_dir() and not any(pasta.iterdir()):
            pasta.rmdir()
    manifesto = {k: v for k, v in sorted(manifesto.items()) if k in usados}
    MANIFESTO.write_text(json.dumps(manifesto, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"{len(manifesto)} fotos; páginas atualizadas: {', '.join(sorted(set(alteradas))) or 'nenhuma'}")


if __name__ == "__main__":
    main()
