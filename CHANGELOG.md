# Changelog - Safe Offshore Website

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto adere ao [Versionamento Semântico](https://semver.org/lang/pt-BR/).

## [2.2.0] - Outubro 2026

### 📸 Painel de fotos gerenciado pelo cliente

#### ✨ Adicionado
- Painel de fotos (Pages CMS, `.pages.yml`): o cliente inclui, ordena e remove fotos de 10 galerias sem mexer em código. Guia de uso em `GUIA-FOTOS.md`
- `content/galerias/*.json`: dados das galerias (projetos da home, logos de clientes, sinalização, hidrelétricas, apoio subaquático, reparo naval, obras civis, documentação, defensas e agulha magnética)
- `scripts/galerias.py`: otimiza as fotos (até 1600px, JPG/PNG + WebP) em `images/galerias/` e reescreve o HTML entre os marcadores `<!-- galeria:nome -->`
- GitHub Action `Publicar site`: gera as galerias a cada push na `main` e envia para a Locaweb por FTP (segredos `FTP_SERVER`, `FTP_USERNAME` e `FTP_PASSWORD`)
- Galeria "Nossos Trabalhos" na página de Defensas, que aparece quando houver fotos
- `web.config` para a Locaweb (IIS): tipo MIME do `.webp` e redirecionamento de http/www para `https://safeoffshore.com.br`
- Fallback no JS: se o servidor não entregar o `.webp`, o navegador usa o `.jpg`/`.png`
- Google Analytics 4 (`G-MGSWB93D6H`) com evento `contato` (WhatsApp, telefone, e-mail e formulário de orçamento)
- Aviso de cookies (LGPD): o Analytics só carrega depois do "Aceitar" (Consent Mode v2, tudo negado por padrão); link "Preferências de cookies" no rodapé para mudar a escolha
- Publicação por `lftp` com FTPS, enviando só os arquivos alterados

---

## [2.1.0] - Outubro 2026

### 🎨 Identidade visual azul + laranja (pedido do cliente)

#### ✨ Adicionado
- Paleta oficial extraída do logo: azul-marinho `#1A3657` e laranja cobre `#CF651F`, com variantes de contraste AA (`--accent-dark`, `--accent-light`)
- Botão flutuante de WhatsApp em todas as páginas, (27) 99620-7455
- Formulário "Solicite um orçamento" em Contato, que envia a mensagem preenchida pelo WhatsApp ou por e-mail
- Rodapé completo e igual nas 16 páginas, com endereço, telefone, WhatsApp e e-mail
- Favicon com o escudo do logo (`favicon.ico`, `icon-192.png`, `apple-touch-icon.png`)
- `sitemap.xml` e `robots.txt`
- Meta description nas 6 páginas que não tinham
- Dados estruturados LocalBusiness com endereço e telefones na home
- Tag canonical em todas as páginas, apontando para `https://www.safeoffshore.com.br/...`

#### 🔧 Alterado
- Botões, menu ativo, sublinhados, ícones, checks e títulos do rodapé passam a usar o laranja da marca
- Imagens das páginas de serviço servidas em WebP com width/height e lazy loading (`odizio_boia_articulada`: de 1,6 MB para 85 KB)
- Fotos de hidrelétricas renomeadas (`hidreletricas-1..5.jpeg`)
- Copyright atualizado para 2015-2026
- Cliente EJA renomeado para Seatrium (antigo Estaleiro Jurong Aracruz)
- Nome do CAMR corrigido para Centro de Auxílios à Navegação Almirante Moraes Rego
- `sitemap.xml` sem `priority` (ignorado pelo Google), com 15 URLs
- H1 da home passa a descrever o serviço ("Sinalização náutica, balizamento e serviços subaquáticos"); o slogan fica acima, como apoio
- Links internos padronizados no formato de diretório (`servicos/` em vez de `servicos/index.html`), igual ao sitemap e ao canonical
- Links do CAMR trocados do domínio antigo `mar.mil.br`, que não resolve mais, para a página do cadastro em `marinha.mil.br`

#### 🐛 Corrigido
- Ícones vazios em "100+ Clientes" e "10+ Anos" na home (símbolos ausentes no sprite)
- Ícones SVG pretos nas páginas internas (faltava `.icon { fill: currentColor }`)
- Logos de clientes quase invisíveis (filtro grayscale + opacidade 70%)
- Menu da página da boia AMRSO-3000 listava só 4 dos 10 serviços
- Flash de azul `#0066cc` e de botão branco na home antes do CSS principal carregar

#### 🗑️ Removido
- Serviço Alpinismo Industrial descontinuado a pedido do cliente: página, menus, formulário e sitemap (fotos movidas para `_material-cliente/`)
- 110 arquivos do site antigo sem uso: CSS e JS legados, `modules/`, `components/`, `fonts/`, bordas e separadores, `escolher-versao.html` e `.tmp`
- Fotos, logos, PDF de apresentação e áudios sem uso foram movidos para `_material-cliente/`, bloqueado no `robots.txt` (não publicar)

---

## [1.0.0] - Outubro 2024

### 🎉 Lançamento Inicial - Reformulação Completa do Site

#### ✨ Adicionado

**Estrutura Geral:**
- Migração completa de XHTML/jQuery para HTML5/CSS3/JavaScript Vanilla
- Sistema de design moderno com CSS Grid e Flexbox
- Variáveis CSS para cores e espaçamentos reutilizáveis
- Responsividade total (mobile-first)
- SEO otimizado com meta tags, Open Graph e Schema.org

**Homepage (index.html):**
- Hero slider automático com 5 imagens
- Navegação por setas, dots, teclado (← →) e touch/swipe
- Seção "Sobre Nós" com 4 cards de features
- Grid de 6 serviços principais
- Galeria de fotos com modal lightbox
- Links para CAMR e Praticagem
- Footer completo com 4 colunas
- Botão "Voltar ao Topo" animado

**Página Quem Somos (about-us/):**
- História da empresa
- Missão, Visão e Valores
- Diferenciais competitivos

**Páginas de Serviços:**
1. **Sinalização Náutica:**
   - Descrição do cadastro CAMR
   - 7 serviços listados
   - Imagem do certificado CAMR (clicável com zoom)
   - Galeria com 6 fotos de trabalhos
   - 3 cards de highlights

2. **Alpinismo Industrial:**
   - 8 tipos de serviços em altura
   - 3 imagens (IRATA + trabalhos)
   - Service highlights

3. **Apoio Subaquático:**
   - Apoio em Obras Civis (13 itens)
   - Inspeções Navais (10 itens)
   - 4 imagens de mergulho

4. **Agulha Magnética e Barômetro:**
   - 6 serviços especializados
   - 3 imagens de certificados

5. **Hidrelétricas:**
   - 7 serviços para usinas
   - 3 imagens de trabalhos

6. **Comércio de Equipamentos:**
   - 7 produtos/equipamentos
   - 2 imagens de produtos

**Página de Clientes (principais-clientes-1/):**
- Grid responsivo com 9 logos de clientes
- Efeito hover (elevação + zoom 1.05x)
- CTA para novos clientes
- Logos em cores (removido filtro grayscale)

**Página de Contato (contato/):**
- 4 cards de informação:
  - Endereço completo
  - 3 telefones (fixo + 2 celulares)
  - E-mail
  - Horário de atendimento
- Formulário funcional (integração com mailto:)
- Google Maps integrado com endereço correto
- Botão "Abrir no Google Maps"
- Layout em 2 colunas (informações + formulário)

**CSS (modern-style.css):**
- 1470+ linhas de CSS moderno
- Variáveis CSS para cores, espaçamentos e sombras
- Seções organizadas (Header, Hero, Services, Gallery, Footer, etc.)
- Animações e transições suaves
- Media queries para responsividade (768px, 992px)
- Classes utilitárias reutilizáveis

**JavaScript (modern-script.js):**
- 512 linhas de código modular
- Funções principais:
  - `initMobileMenu()` - Menu hamburger
  - `initHeroSlider()` - Slider automático
  - `initBackToTop()` - Botão voltar ao topo
  - `initGalleryModal()` - Modal de imagens com zoom
  - `initSmoothScroll()` - Scroll suave
  - `initHeaderScroll()` - Header diminui no scroll
  - `initContactForm()` - Handler do formulário
  - `animateOnScroll()` - Animações ao rolar
- Sem dependências externas (Vanilla JS)

**Funcionalidades Interativas:**
- Gallery modal com navegação entre imagens
- Suporte a teclado (ESC, ← →) no modal
- Click/tap em todas as imagens para zoom
- Efeitos hover em cards e imagens
- Menu dropdown animado
- Transições suaves em todos os elementos

#### 🔧 Corrigido

**Problemas de Imagens:**
- ✅ Descoberto padrão de nomenclatura `*82b7.*` em todos os arquivos
- ✅ Corrigidos caminhos de todas as imagens (40+ arquivos)
- ✅ Adicionada classe `.clickable-image` para imagens individuais
- ✅ Modal de zoom funcionando em todas as páginas de serviço

**Header:**
- ✅ Corrigido comportamento de scroll (header crescia e não voltava)
- ✅ Mudança de inline styles para sistema de classes (`.scrolled`)
- ✅ Transição suave de altura do logo (60px → 50px)

**Navegação de Imagens:**
- ✅ Corrigido bug de duplo clique nas setas do modal
- ✅ Removida duplicação de seletor `.service-images-grid img`

**Legenda de Imagem:**
- ✅ Certificado CAMR: legenda agora aparece abaixo (não ao lado)
- ✅ Adicionado `display: block` e `margin: 0 auto` na imagem

**Mapa Google Maps:**
- ✅ Corrigido localização (estava no meio do mar)
- ✅ URL atualizada com endereço correto: Rua Fortunato Abreu Gágno, 728
- ✅ Adicionado botão "Abrir no Google Maps"

**Logos de Clientes:**
- ✅ Removido filtro grayscale (imagens agora coloridas)
- ✅ Adicionado efeito zoom no hover (1.05x)
- ✅ Ajustado tamanho das imagens (max-height: 140px)

#### 📝 Documentação

- ✅ Criado `DOCUMENTACAO.md` completo (estrutura, funcionalidades, padrões)
- ✅ Atualizado `README.md` com quick start e informações essenciais
- ✅ Criado `CHANGELOG.md` (este arquivo)
- ✅ Documentadas todas as classes CSS importantes
- ✅ Documentadas todas as funções JavaScript
- ✅ Listados todos os arquivos criados/modificados

#### 🎨 Design

**Paleta de Cores:**
- Primary: #1a5490 (Azul marinho)
- Secondary: #00a8e8 (Azul claro)
- Accent: #ff6b35 (Laranja)
- Text Dark: #2c3e50
- Text Gray: #7f8c8d
- BG Light: #f8f9fa

**Tipografia:**
- Headings: Poppins (Google Fonts)
- Body: Roboto (Google Fonts)
- Ícones: Font Awesome 6.4.0

**Breakpoints:**
- Desktop: > 992px
- Tablet: 768px - 992px
- Mobile: < 768px
- Small Mobile: < 480px

#### 🚀 Performance

- Lazy loading em todas as imagens (`loading="lazy"`)
- Preconnect para Google Fonts
- Debounce em eventos de scroll/resize
- CSS otimizado com variáveis
- JavaScript modular e eficiente
- Sem bibliotecas pesadas (Vanilla JS)

#### ♿ Acessibilidade

- Tags semânticas HTML5
- Alt text em todas as imagens
- ARIA labels em botões
- Navegação por teclado funcional
- Contraste adequado de cores
- Focus states visíveis

#### 📊 SEO

- Meta tags otimizadas
- Open Graph (Facebook)
- Twitter Cards
- Schema.org (JSON-LD)
- URLs amigáveis
- Heading hierarchy correta (h1 → h2 → h3)
- Alt text descritivo em imagens

---

## [Próximas Versões]

### 🔮 Planejado para v1.1.0

#### A Implementar
- [ ] Sitemap.xml
- [ ] Robots.txt
- [ ] Google Analytics / GA4
- [ ] WhatsApp Button flutuante
- [ ] Minificação CSS/JS para produção
- [ ] Otimização de imagens (WebP)
- [ ] Service Worker (PWA)
- [ ] Backend real para formulário

#### A Considerar
- [ ] Sistema de blog/notícias
- [ ] Área administrativa
- [ ] Multi-idioma (PT/EN)
- [ ] Chat ao vivo
- [ ] Depoimentos de clientes
- [ ] Portfólio expandido
- [ ] Vídeos institucionais
- [ ] Certificações (ISO)

---

## Tipos de Mudanças

- `✨ Adicionado` - Novas funcionalidades
- `🔧 Corrigido` - Correções de bugs
- `🔄 Alterado` - Mudanças em funcionalidades existentes
- `🗑️ Removido` - Funcionalidades removidas
- `🔒 Segurança` - Correções de vulnerabilidades
- `📝 Documentação` - Apenas mudanças em documentação
- `🎨 Design` - Mudanças visuais/estéticas
- `🚀 Performance` - Melhorias de performance
- `♿ Acessibilidade` - Melhorias de acessibilidade

---

**Formato de Versões:** [MAJOR.MINOR.PATCH]
- **MAJOR:** Mudanças incompatíveis na API/estrutura
- **MINOR:** Novas funcionalidades compatíveis
- **PATCH:** Correções de bugs compatíveis

---

*Última Atualização: Outubro 2024*
