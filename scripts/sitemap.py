"""Gera o sitemap.xml com as páginas em português e inglês e os pares de idioma (hreflang).

lastmod = data do último commit da página (ou hoje, se ela ainda não foi commitada).
Uso: python scripts/sitemap.py
"""
import datetime
import subprocess
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
BASE = "https://safeoffshore.com.br/"
IGNORAR = ("images/", "uploads/", "content/", "scripts/", "_material-cliente/", "reports/", "research_notes/", "node_modules/")

# página em português -> equivalente em inglês
PARES = {
    "": "en/",
    "about-us/": "en/about-us/",
    "principais-clientes-1/": "en/clients/",
    "contato/": "en/contact/",
    "servicos/": "en/services/",
    "servicos/sinalizacao-nautica/": "en/services/aids-to-navigation/",
    "servicos/comercio-de-equipamentos-de-sinalizacao-nautica/": "en/services/navigation-aids-equipment/",
    "servicos/comercio-de-equipamentos-de-sinalizacao-nautica/boia-amarracao-amrso-3000/": "en/services/navigation-aids-equipment/amrso-3000-mooring-buoy/",
    "servicos/documentacao-marinha/": "en/services/brazilian-navy-permits/",
    "servicos/defensas-portos/": "en/services/port-fenders/",
    "servicos/apoio-subaquatico/": "en/services/underwater-services/",
    "servicos/obras-civis/": "en/services/underwater-civil-works/",
    "servicos/reparo-naval/": "en/services/underwater-ship-repair/",
    "servicos/hidreletricas/": "en/services/hydropower-plants/",
    "servicos/agulha-magnetica-e-barometro-aneroide/": "en/services/magnetic-compass-adjustment/",
}


def lastmod(arquivo):
    saida = subprocess.run(["git", "log", "-1", "--format=%cs", "--", arquivo], cwd=RAIZ, capture_output=True, text=True).stdout.strip()
    pendente = subprocess.run(["git", "status", "--porcelain", "--", arquivo], cwd=RAIZ, capture_output=True, text=True).stdout.strip()
    return datetime.date.today().isoformat() if (pendente or not saida) else saida


def main():
    paginas = sorted(p.relative_to(RAIZ).as_posix()[: -len("index.html")]
                     for p in RAIZ.rglob("index.html")
                     if not p.relative_to(RAIZ).as_posix().startswith(IGNORAR))
    existentes = set(paginas)
    inverso = {en: pt for pt, en in PARES.items()}
    linhas = ['<?xml version="1.0" encoding="UTF-8"?>',
              '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for pagina in paginas:
        pt = pagina if pagina in PARES else inverso.get(pagina)
        en = PARES.get(pt) if pt is not None else None
        linhas += ["  <url>", f"    <loc>{BASE}{pagina}</loc>", f"    <lastmod>{lastmod(pagina + 'index.html')}</lastmod>"]
        if pt is not None and en in existentes and pt in existentes:
            linhas += [f'    <xhtml:link rel="alternate" hreflang="pt-BR" href="{BASE}{pt}"/>',
                       f'    <xhtml:link rel="alternate" hreflang="en" href="{BASE}{en}"/>',
                       f'    <xhtml:link rel="alternate" hreflang="x-default" href="{BASE}{pt}"/>']
        linhas.append("  </url>")
    linhas.append("</urlset>")
    (RAIZ / "sitemap.xml").write_text("\n".join(linhas) + "\n", encoding="utf-8")
    print(f"sitemap.xml: {len(paginas)} páginas")


if __name__ == "__main__":
    main()
