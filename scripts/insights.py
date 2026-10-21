"""Gera a central de artigos em inglês (/en/insights/) a partir de content/insights/*.md.

Cada artigo é um arquivo Markdown com cabeçalho YAML:

    ---
    title: Título do artigo (H1)
    title_tag: Título para o Google, até 60 caracteres
    description: Descrição para o Google, até 155 caracteres
    summary: Resumo curto para o card no índice
    date: 2026-10-21            # publicação
    reviewed: 2026-10-21        # última revisão técnica
    service_url: en/services/underwater-ship-repair/
    service_label: Underwater Ship Repair
    ---
    Texto em Markdown...

O cabeçalho, o menu e o rodapé vêm de LAYOUT (uma página em inglês já existente), para que
os artigos acompanhem qualquer mudança no menu. Uso: python scripts/insights.py
(requer markdown e pyyaml)
"""
import html
import json
import posixpath
import re
from pathlib import Path

import markdown
import yaml

RAIZ = Path(__file__).resolve().parent.parent
FONTE = RAIZ / "content" / "insights"
DESTINO = "en/insights/"
LAYOUT = "en/about-us/index.html"
BASE = "https://safeoffshore.com.br/"
MESES = ["January", "February", "March", "April", "May", "June", "July", "August",
         "September", "October", "November", "December"]


def data_longa(data):
    return f"{data.day} {MESES[data.month - 1]} {data.year}"


def realocar(trecho, de_dir, para_dir):
    """Reescreve caminhos relativos de um trecho HTML escrito para de_dir, para valer em para_dir."""
    def corrigir(m):
        attr, url = m.group(1), m.group(2)
        if url.startswith(("http", "mailto:", "tel:", "#", "data:", "/")) or not url:
            return m.group(0)
        caminho = posixpath.normpath(posixpath.join(de_dir, url))
        novo = posixpath.relpath(caminho, para_dir.rstrip("/") or ".")
        if url.endswith("/"):
            novo = "./" if novo == "." else novo + "/"
        return f'{attr}="{novo}"'
    return re.sub(r'\b(href|src|srcset)="([^"]*)"', corrigir, trecho)


def layout(para_dir):
    """(topo, rodape): do <body> até </header> e do <footer> até o fim, com o menu em Insights."""
    texto = (RAIZ / LAYOUT).read_text(encoding="utf-8")
    de_dir = posixpath.dirname(LAYOUT) + "/"
    inicio_body = texto.index("<body>")
    fim_header = texto.index("</header>") + len("</header>")
    topo = texto[inicio_body:fim_header]
    rodape = texto[texto.index('    <footer class="footer">'):]
    topo = topo.replace(' class="active"', "").replace('class="dropdown-toggle active"', 'class="dropdown-toggle"')
    topo = re.sub(r'(<li><a href="[^"]*insights/")>', r'\1 class="active">', topo)
    # artigos só existem em inglês: o seletor PT leva à página inicial em português
    topo = re.sub(r'(<li class="lang-switch"><a href=")[^"]*(")', lambda m: m.group(1) + posixpath.relpath(".", de_dir.rstrip("/")) + "/" + m.group(2), topo)
    return realocar(topo, de_dir, para_dir), realocar(rodape, de_dir, para_dir)


def cabecalho_html(para_dir, titulo_aba, descricao, url, og_tipo, jsonld):
    p = posixpath.relpath(".", para_dir.rstrip("/")) + "/"
    e = html.escape
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Google tag (gtag.js): só carrega depois do "Aceitar" no aviso de cookies (LGPD) -->
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('consent', 'default', {{analytics_storage: 'denied', ad_storage: 'denied', ad_user_data: 'denied', ad_personalization: 'denied'}});
      gtag('js', new Date());
      gtag('config', 'G-MGSWB93D6H');
      function carregarAnalytics() {{
        gtag('consent', 'update', {{analytics_storage: 'granted'}});
        var s = document.createElement('script');
        s.async = true;
        s.src = 'https://www.googletagmanager.com/gtag/js?id=G-MGSWB93D6H';
        document.head.appendChild(s);
      }}
      try {{ if (localStorage.getItem('cookies-consentimento') === 'aceito') carregarAnalytics(); }} catch (e) {{}}
    </script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{e(titulo_aba)}</title>
    <link rel="canonical" href="{url}">
    <meta name="description" content="{e(descricao)}">
    <meta property="og:type" content="{og_tipo}">
    <meta property="og:title" content="{e(titulo_aba)}">
    <meta property="og:description" content="{e(descricao)}">
    <meta property="og:url" content="{url}">
    <meta property="og:image" content="{BASE}attachments/Logo/LOGO-01T-PNG.png">
    <meta property="og:locale" content="en_US">
    <link rel="icon" href="{p}favicon.ico" sizes="any">
    <link rel="icon" type="image/png" href="{p}icon-192.png" sizes="192x192">
    <link rel="apple-touch-icon" href="{p}apple-touch-icon.png">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&family=Roboto:wght@300;400;500;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="{p}css/safeoffshore-style.css">
    <script type="application/ld+json">
{json.dumps(jsonld, ensure_ascii=False, indent=4)}
    </script>
</head>
'''


def fim_pagina(rodape):
    return "\n\n" + rodape


def ler_artigos():
    artigos = []
    for arquivo in sorted(FONTE.glob("*.md")):
        texto = arquivo.read_text(encoding="utf-8")
        _, frente, corpo = texto.split("---", 2)
        meta = yaml.safe_load(frente)
        for campo in ("title", "title_tag", "description", "summary", "date", "service_url", "service_label"):
            if not meta.get(campo):
                raise SystemExit(f"{arquivo.name}: falta o campo '{campo}'")
        meta["slug"] = arquivo.stem
        meta["reviewed"] = meta.get("reviewed") or meta["date"]
        meta["html"] = markdown.markdown(corpo, extensions=["tables", "sane_lists", "attr_list"])
        artigos.append(meta)
    return sorted(artigos, key=lambda a: a["date"], reverse=True)


def pagina_artigo(a):
    para_dir = f"{DESTINO}{a['slug']}/"
    url = BASE + para_dir
    topo, rodape = layout(para_dir)
    rel = lambda alvo: posixpath.relpath(alvo.rstrip("/"), para_dir.rstrip("/")) + "/"
    jsonld = {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "Article", "headline": a["title"], "description": a["description"],
             "datePublished": str(a["date"]), "dateModified": str(a["reviewed"]), "inLanguage": "en",
             "mainEntityOfPage": url, "image": BASE + "attachments/Logo/LOGO-01T-PNG.png",
             "author": {"@type": "Organization", "name": "Safe Offshore", "url": BASE + "en/"},
             "publisher": {"@type": "Organization", "name": "Safe Offshore",
                           "logo": {"@type": "ImageObject", "url": BASE + "attachments/Logo/LOGO-01T-PNG.png"}}},
            {"@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE + "en/"},
                {"@type": "ListItem", "position": 2, "name": "Insights", "item": BASE + DESTINO},
                {"@type": "ListItem", "position": 3, "name": a["title"], "item": url}]},
        ],
    }
    e = html.escape
    corpo = f'''<body>{topo[len("<body>"):]}

    <section class="page-header">
        <div class="page-header-overlay"></div>
        <div class="container">
            <h1 class="page-title article-title">{e(a["title"])}</h1>
            <nav class="breadcrumb" aria-label="Breadcrumb">
                <a href="{rel('en/')}">Home</a>
                <span class="separator">/</span>
                <a href="{rel(DESTINO)}">Insights</a>
            </nav>
        </div>
    </section>

    <section class="article-section">
        <div class="container article-layout">
            <article class="article-body">
                <p class="article-meta">Last reviewed {data_longa(a["reviewed"])}</p>
{a["html"]}
            </article>
            <aside class="article-aside">
                <div class="article-cta">
                    <h2>Need this service in Brazil?</h2>
                    <p>Safe Offshore is based in Vitória, Espírito Santo, and works with ports, terminals, shipowners and agents.</p>
                    <a href="{rel(a["service_url"])}" class="btn btn-primary">{e(a["service_label"])}</a>
                    <a href="{rel('en/contact/')}" class="btn btn-outline">Request a quote</a>
                </div>
            </aside>
        </div>
    </section>
'''
    return cabecalho_html(para_dir, a["title_tag"], a["description"], url, "article", jsonld) + corpo + fim_pagina(rodape)


def pagina_indice(artigos):
    para_dir = DESTINO
    url = BASE + para_dir
    topo, rodape = layout(para_dir)
    e = html.escape
    jsonld = {"@context": "https://schema.org", "@type": "CollectionPage", "name": "Insights",
              "url": url, "inLanguage": "en",
              "hasPart": [{"@type": "Article", "headline": a["title"], "url": f"{url}{a['slug']}/"} for a in artigos]}
    cards = "\n".join(f'''                <article class="insight-card">
                    <p class="insight-date">{data_longa(a["date"])}</p>
                    <h2><a href="{a["slug"]}/">{e(a["title"])}</a></h2>
                    <p>{e(a["summary"])}</p>
                    <a href="{a["slug"]}/" class="insight-link" aria-label="Read: {e(a["title"])}">Read the article</a>
                </article>''' for a in artigos)
    corpo = f'''<body>{topo[len("<body>"):]}

    <section class="page-header">
        <div class="page-header-overlay"></div>
        <div class="container">
            <h1 class="page-title">Insights</h1>
            <nav class="breadcrumb" aria-label="Breadcrumb">
                <a href="../">Home</a>
                <span class="separator">/</span>
                <span class="current">Insights</span>
            </nav>
        </div>
    </section>

    <section class="article-section">
        <div class="container">
            <p class="insights-intro">Practical guides for shipowners, ship managers, port operators and contractors who need maritime services in Brazil: what the Brazilian rules require, which documents to prepare and how to plan the job.</p>
            <div class="insights-grid">
{cards}
            </div>
        </div>
    </section>
'''
    titulo = "Insights: Maritime Services in Brazil | Safe Offshore"
    descricao = "Guides on Brazilian maritime rules and services: hull cleaning, commercial diving, aids to navigation, compass adjustment and Navy permits."
    return cabecalho_html(para_dir, titulo, descricao, url, "website", jsonld) + corpo + fim_pagina(rodape)


def main():
    artigos = ler_artigos()
    destino = RAIZ / DESTINO
    destino.mkdir(parents=True, exist_ok=True)
    for a in artigos:
        (destino / a["slug"]).mkdir(exist_ok=True)
        (destino / a["slug"] / "index.html").write_text(pagina_artigo(a), encoding="utf-8")
    (destino / "index.html").write_text(pagina_indice(artigos), encoding="utf-8")
    slugs = {a["slug"] for a in artigos}
    for pasta in destino.iterdir():  # artigo removido -> página removida
        if pasta.is_dir() and pasta.name not in slugs:
            for f in pasta.iterdir():
                f.unlink()
            pasta.rmdir()
    print(f"{len(artigos)} artigos em /{DESTINO}")


if __name__ == "__main__":
    main()
