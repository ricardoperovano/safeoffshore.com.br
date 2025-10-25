# Documentação - Safe Offshore Website

## 📋 Sumário Executivo

Este projeto é a reformulação completa do website da **Safe Offshore Serviços Marítimos**, migrando de um site antigo (XHTML + jQuery + Parallels Presence Builder) para uma versão moderna com **HTML5, CSS3 e JavaScript Vanilla**.

**Período de Desenvolvimento:** Outubro 2024
**Status:** Versão moderna completamente funcional
**URL Original:** http://www.safeoffshore.com.br/
**Localização do Projeto:** `/home/luiz-ricardo/projects/safeoffshore/`

---

## 🏗️ Estrutura do Projeto

```
safeoffshore/
├── index.html                          # Homepage moderna
├── about-us/
│   └── index.html                      # Página Quem Somos
├── servicos/
│   ├── index.html                      # Listagem de Serviços
│   ├── sinalizacao-nautica/
│   │   └── index.html                  # Sinalização Náutica (com imagens CAMR + 6 fotos)
│   ├── comercio-de-equipamentos-de-sinalizacao-nautica/
│   │   └── index.html                  # Comércio de Equipamentos (2 imagens de produtos)
│   ├── apoio-subaquatico/
│   │   └── index.html                  # Apoio Subaquático (4 imagens de mergulho)
│   ├── agulha-magnetica-e-barometro-aneroide/
│   │   └── index.html                  # Agulha Magnética (3 certificados)
│   ├── hidreletricas/
│   │   └── index.html                  # Hidrelétricas (3 imagens)
│   └── alpinismo-industrial/
│       └── index.html                  # Alpinismo Industrial (3 imagens IRATA)
├── principais-clientes-1/
│   └── index.html                      # Página de Clientes (9 logos)
├── contato/
│   └── index.html                      # Página de Contato (formulário + mapa)
├── css/
│   └── modern-style.css                # CSS principal (1470+ linhas)
├── js/
│   └── modern-script.js                # JavaScript principal (512 linhas)
├── attachments/
│   ├── Logo/
│   │   ├── LOGO-01T-PNG.png           # Logo principal
│   │   └── LOGO-02T-PNG82b7.png       # Logo alternativo
│   ├── Image/                          # Imagens de serviços e certificados
│   └── Slider/                         # Imagens de trabalhos/projetos
├── safeoffshore.com.br/                # Site antigo (backup/referência)
├── DOCUMENTACAO.md                     # Este arquivo
└── README.md                           # Instruções básicas
```

---

## 🎨 Tecnologias Utilizadas

### Frontend
- **HTML5:** Estrutura semântica moderna
- **CSS3:**
  - CSS Grid e Flexbox para layouts
  - CSS Custom Properties (variáveis)
  - Animations e Transitions
  - Mobile-first design
- **JavaScript (Vanilla ES6+):**
  - Sem dependências de bibliotecas
  - Modular e reutilizável
  - Event listeners modernos

### Bibliotecas Externas (CDN)
- **Google Fonts:** Poppins e Roboto
- **Font Awesome 6.4.0:** Ícones

### SEO
- Meta tags otimizadas
- Open Graph (Facebook)
- Twitter Cards
- Schema.org (JSON-LD)
- Sitemap XML (a ser criado)

---

## 📄 Páginas Implementadas

### 1. Homepage (`index.html`)
**Status:** ✅ Completo

**Seções:**
- Header fixo com menu responsivo
- Hero Slider (3 slides com auto-play, navegação por setas/dots/teclado/touch)
- Sobre Nós (resumo)
- Serviços em destaque (6 cards)
- Galeria de fotos (modal lightbox)
- Links úteis (CAMR, Praticagem)
- Footer completo (4 colunas)
- Botão voltar ao topo

**Funcionalidades:**
- Slider automático (5s por slide)
- Menu dropdown para serviços
- Menu hamburger mobile
- Gallery modal com navegação
- Header que diminui no scroll

---

### 2. Quem Somos (`about-us/index.html`)
**Status:** ✅ Completo

**Conteúdo:**
- História da empresa
- Missão, Visão e Valores
- Diferenciais competitivos

---

### 3. Serviços (`servicos/index.html`)
**Status:** ✅ Completo

**Listagem de 6 serviços:**
1. Sinalização Náutica
2. Comércio de Equipamentos
3. Apoio Subaquático
4. Agulha Magnética e Barômetro
5. Hidrelétricas
6. Alpinismo Industrial

---

### 4. Sinalização Náutica (`servicos/sinalizacao-nautica/index.html`)
**Status:** ✅ Completo

**Conteúdo Específico:**
- Descrição do cadastro CAMR
- Lista de serviços oferecidos (7 itens)
- Certificação CAMR (imagem: `Imagem382b7.png`)
- Galeria "Nossos Trabalhos" (6 fotos)
- Service highlights (3 cards)
- CTA para contato

**Imagens:**
- `attachments/Image/Imagem382b7.png` (Certificado CAMR)
- `attachments/Slider/5cc636a7-8a23-92dc-adff-ed407c032387/IMG-20150526-WA000382b7.jpg`
- `attachments/Slider/5cc636a7-8a23-92dc-adff-ed407c032387/IMG-20150526-WA000482b7.jpg`
- `attachments/Slider/5cc636a7-8a23-92dc-adff-ed407c032387/05b5ccb8-7c7e-d30c-cfe1-4252e0d8b54a82b7.jpg`
- `attachments/Slider/5cc636a7-8a23-92dc-adff-ed407c032387/IMG_20170725_13214800282b7.jpg`
- `attachments/Slider/5cc636a7-8a23-92dc-adff-ed407c032387/IMG_20170722_09104752182b7.jpg`
- `attachments/Slider/5cc636a7-8a23-92dc-adff-ed407c032387/IMG_20170725_13140929682b7.jpg`

---

### 5. Alpinismo Industrial (`servicos/alpinismo-industrial/index.html`)
**Status:** ✅ Completo

**Conteúdo Específico:**
- Descrição de trabalhos em altura
- Lista de serviços (8 itens)
- Certificações IRATA
- Galeria (3 imagens)
- Service highlights

**Imagens:**
- `attachments/Image/IRATA82b7.jpg`
- `attachments/Image/134150935949116NR_3582b7.jpg`
- `attachments/Image/207f75_b44c5300b80a4f83ad8c5a77e57a1b6a82b7.gif`

---

### 6. Apoio Subaquático (`servicos/apoio-subaquatico/index.html`)
**Status:** ✅ Completo

**Conteúdo Específico:**
- Apoio em Obras Civis (13 itens)
- Inspeções Navais (10 itens)
- Galeria (4 imagens de mergulho)

**Imagens:**
- `attachments/Slider/23db7e57-1392-c32d-cea9-3e94ebdac28b/merg282b7.png`
- `attachments/Slider/23db7e57-1392-c32d-cea9-3e94ebdac28b/merg382b7.png`
- `attachments/Slider/23db7e57-1392-c32d-cea9-3e94ebdac28b/Imagem182b7.jpg`
- `attachments/Slider/23db7e57-1392-c32d-cea9-3e94ebdac28b/Imagem382b7.jpg`

---

### 7. Agulha Magnética (`servicos/agulha-magnetica-e-barometro-aneroide/index.html`)
**Status:** ✅ Completo

**Conteúdo Específico:**
- Serviços de compensação e aferição (6 itens)
- Galeria de certificados (3 imagens)

**Imagens:**
- `attachments/Image/certificado_182b7.png`
- `attachments/Image/certificado82b7.png`
- `attachments/Image/ns-7.5-40082b7.jpg`

---

### 8. Hidrelétricas (`servicos/hidreletricas/index.html`)
**Status:** ✅ Completo

**Conteúdo Específico:**
- Serviços para usinas (7 itens)
- Galeria (3 imagens)

**Imagens:**
- `attachments/Image/Imagem582b7.png`
- `attachments/Image/Imagem682b7.png`
- `attachments/Image/Imagem482b7.png`

---

### 9. Comércio de Equipamentos (`servicos/comercio-de-equipamentos-de-sinalizacao-nautica/index.html`)
**Status:** ✅ Completo

**Conteúdo Específico:**
- Equipamentos fornecidos (7 itens)
- Galeria de produtos (2 imagens)

**Imagens:**
- `attachments/Image/linhapamarela82b7.png`
- `attachments/Image/faroletes82b7.png`

---

### 10. Principais Clientes (`principais-clientes-1/index.html`)
**Status:** ✅ Completo

**Funcionalidades:**
- Grid responsivo com 9 logos de clientes
- Efeito hover (elevação + zoom)
- CTA para novos clientes

**Clientes:**
1. Technip (`technip82b7.jpg`)
2. Jurong Shipyard (`LOGO-JURONG82b7.jpg`)
3. Camorim (`camorim82b7.jpg`)
4. Dratec (`Dratec82b7.jpg`)
5. Jan De Nul (`jandenul82b7.jpg`)
6. Astro Marítima (`astromaritima82b7.jpg`)
7. OAS (`OAS82b7.jpg`)
8. Andrade Gutierrez (`andrade-gutierrez82b7.png`)
9. Estacon (`estacon82b7.jpg`)

---

### 11. Contato (`contato/index.html`)
**Status:** ✅ Completo

**Informações de Contato:**
- **Endereço:** Rua Fortunato Abreu Gágno, 728, Sala 1, Jardim Camburi, Vitória - ES, CEP: 29090-200
- **Telefones:**
  - (27) 3376-4732
  - (27) 9.9620-7455 - Alcântara
  - (27) 9.9740-7072 - Rhoger
- **E-mail:** contato@safeoffshore.com.br
- **Horário:** Segunda a Sexta: 08:00 - 18:00, Sábado: 08:00 - 12:00

**Funcionalidades:**
- 4 cards de informação (endereço, telefone, e-mail, horário)
- Formulário de contato funcional (abre cliente de e-mail)
- Mapa do Google Maps integrado
- Layout em 2 colunas (info + formulário)
- Botão "Abrir no Google Maps"

---

## 🎯 Funcionalidades Implementadas

### Header & Navegação
- **Header Fixo:** Permanece visível durante scroll
- **Efeito Scroll:** Diminui altura quando rola (padding 1rem → 0.5rem, logo 60px → 50px)
- **Menu Dropdown:** Submenu de serviços com animação
- **Menu Mobile:** Hamburger menu responsivo (< 992px)
- **Active State:** Destaca página atual no menu

### Hero Slider
- **Auto-play:** Troca automática a cada 5 segundos
- **Navegação:**
  - Setas (anterior/próximo)
  - Dots (indicadores clicáveis)
  - Teclado (← →)
  - Touch/Swipe (mobile)
- **Pausa no Hover:** Para automação ao passar mouse
- **Transição Suave:** Fade in/out com CSS

### Gallery Modal (Lightbox)
- **Zoom de Imagens:** Clique em qualquer imagem para ampliar
- **Navegação:**
  - Setas laterais
  - Teclado (← → ESC)
  - Clique fora para fechar
- **Seletores:** `.gallery-item`, `.service-image-item`, `.clickable-image`
- **Efeito Hover:** Zoom 1.05x nas imagens

### Formulário de Contato
- **Validação:** Campos obrigatórios marcados com *
- **Integração:** Abre cliente de e-mail (mailto:) com dados preenchidos
- **Campos:**
  - Nome Completo *
  - E-mail *
  - Telefone
  - Assunto *
  - Mensagem *
- **Feedback:** Alert confirmando envio

### Back to Top
- **Aparece:** Após scroll > 300px
- **Animação:** Fade in/out
- **Comportamento:** Scroll suave ao topo

### Responsividade
- **Breakpoints:**
  - Desktop: > 992px
  - Tablet: 768px - 992px
  - Mobile: < 768px
  - Small Mobile: < 480px
- **Grid Adaptativo:** Auto-fit com minmax
- **Menu Mobile:** Hamburger < 992px

---

## 🎨 CSS - Estrutura e Padrões

### Variáveis CSS (`:root`)
```css
--primary-color: #1a5490;        /* Azul marinho */
--secondary-color: #00a8e8;      /* Azul claro */
--accent-color: #ff6b35;         /* Laranja */
--text-dark: #2c3e50;
--text-gray: #7f8c8d;
--text-light: #ffffff;
--bg-white: #ffffff;
--bg-light: #f8f9fa;
--bg-dark: #2c3e50;

--spacing-xs: 0.5rem;
--spacing-sm: 1rem;
--spacing-md: 1.5rem;
--spacing-lg: 2rem;
--spacing-xl: 3rem;

--shadow-sm: 0 2px 4px rgba(0, 0, 0, 0.1);
--shadow-md: 0 4px 6px rgba(0, 0, 0, 0.1);
--shadow-lg: 0 8px 15px rgba(0, 0, 0, 0.15);

--transition-normal: all 0.3s ease;
--transition-fast: all 0.2s ease;
```

### Seções CSS (modern-style.css)
1. **Reset & Base Styles** (linhas 1-89)
2. **Header & Navigation** (90-250)
3. **Hero Section** (251-350)
4. **Buttons** (351-400)
5. **Services Section** (401-550)
6. **Gallery** (551-650)
7. **Footer** (651-750)
8. **Page Header** (751-850)
9. **About Section** (851-950)
10. **Service Pages** (951-1050)
11. **Service Highlights** (1051-1150)
12. **Service Images Grid** (1151-1213)
13. **Clients Section** (1215-1302)
14. **Contact Section** (1304-1469)
15. **Animations** (1471-1530)

### Classes Importantes

#### Layout
- `.container`: Max-width 1200px, padding lateral
- `.section-header`: Cabeçalho de seção centralizado
- `.section-title`: Título com underline
- `.title-underline`: Linha decorativa azul

#### Cards
- `.service-card`: Card de serviço com hover
- `.feature-card`: Card de destaque
- `.client-item`: Card de logo de cliente
- `.contact-info-item`: Card de informação de contato

#### Imagens
- `.service-images-grid`: Grid de imagens (auto-fit, minmax 250px)
- `.service-image-item`: Container de imagem clicável
- `.clickable-image`: Imagem individual clicável
- `.gallery-item`: Item de galeria na homepage

#### Formulários
- `.form-group`: Container de campo de formulário
- `.contact-form`: Formulário de contato
- `.btn-primary`: Botão primário (azul)
- `.btn-secondary`: Botão secundário (cinza)

---

## 🔧 JavaScript - Funcionalidades

### Estrutura (modern-script.js)

**1. Mobile Menu (`initMobileMenu`)** - Linhas 1-45
- Toggle do menu hamburger
- Fecha ao clicar fora
- Fecha ao clicar em link

**2. Hero Slider (`initHeroSlider`)** - Linhas 87-199
- Auto-play (5s)
- Navegação por setas, dots, teclado, touch
- Pausa no hover

**3. Back to Top (`initBackToTop`)** - Linhas 202-221
- Mostra botão após 300px scroll
- Scroll suave ao topo

**4. Gallery Modal (`initGalleryModal`)** - Linhas 224-306
- Lightbox para imagens
- Navegação entre imagens
- Suporta `.gallery-item`, `.service-image-item`, `.clickable-image`

**5. Smooth Scroll (`initSmoothScroll`)** - Linhas 309-335
- Scroll suave para âncoras
- Offset de 80px (altura do header)

**6. Header Scroll (`initHeaderScroll`)** - Linhas 338-352
- Adiciona classe `.scrolled` após 100px scroll
- CSS controla animação

**7. Lazy Loading** - Linhas 355-371
- Carrega imagens com `loading="lazy"`
- Usa IntersectionObserver

**8. Animation on Scroll (`animateOnScroll`)** - Linhas 373-398
- Anima elementos ao entrarem na viewport
- Fade in + slide up

**9. Form Validation (`initFormValidation`)** - Linhas 401-462
- Valida campos obrigatórios
- Adiciona classe `.error` em campos inválidos

**10. Contact Form Handler (`initContactForm`)** - Linhas 470-507
- Captura dados do formulário
- Cria mailto link
- Abre cliente de e-mail

---

## 🐛 Problemas Resolvidos

### 1. Imagens com Nomes Incorretos
**Problema:** Imagens não carregavam (exemplo: `IRATA.jpg` ao invés de `IRATA82b7.jpg`)
**Solução:** Descoberto padrão de nomenclatura com sufixo `82b7` em todos os arquivos

### 2. Header Crescendo ao Scroll
**Problema:** Header aplicava estilos inline que não revertiam
**Solução:** Mudança para sistema de classes (`.scrolled`) controlado por CSS

### 3. Navegação de Imagens no Modal
**Problema:** Necessário clicar 2x nas setas para mudar imagem
**Solução:** Remover duplicação de seletor (`.service-images-grid img` estava duplicando)

### 4. Imagem do Certificado CAMR não Ampliava
**Problema:** Imagem não tinha classe correta para modal
**Solução:** Adicionar classe `.clickable-image`

### 5. Legenda "Cadastro CAMR" ao Lado da Imagem
**Problema:** `<p>` inline com a imagem
**Solução:** Adicionar `display: block; margin: 0 auto` na imagem

### 6. Mapa no Meio do Mar
**Problema:** URL do Google Maps com coordenadas incorretas
**Solução:** Usar endereço completo na URL: `q=Rua+Fortunato+Abreu+Gagno,728,Jardim+Camburi,Vitoria,ES,29090-200`

---

## 📁 Padrões de Nomenclatura

### Arquivos de Imagem
- **Padrão:** `nome_do_arquivo82b7.extensão`
- **Exemplos:**
  - `IRATA82b7.jpg`
  - `technip82b7.jpg`
  - `Imagem382b7.png`
  - `certificado82b7.png`

### Estrutura de Diretórios
- **Páginas:** `/nome-da-pagina/index.html`
- **Serviços:** `/servicos/nome-do-servico/index.html`
- **Assets:** `/attachments/tipo/arquivo82b7.ext`

### Classes CSS (BEM-like)
- **Blocos:** `.service-card`, `.client-item`, `.contact-form`
- **Elementos:** `.service-card-title`, `.client-item-logo`
- **Modificadores:** `.btn-primary`, `.nav-menu-active`

---

## ✅ Checklist de Funcionalidades

### Homepage
- [x] Hero slider funcional (auto-play, navegação)
- [x] Seção sobre
- [x] Grid de serviços (6 cards)
- [x] Galeria de fotos (modal)
- [x] Links úteis
- [x] Footer completo
- [x] Menu responsivo

### Páginas de Serviço
- [x] Sinalização Náutica (7 imagens)
- [x] Alpinismo Industrial (3 imagens)
- [x] Apoio Subaquático (4 imagens)
- [x] Agulha Magnética (3 imagens)
- [x] Hidrelétricas (3 imagens)
- [x] Comércio de Equipamentos (2 imagens)
- [x] Modal de zoom para todas as imagens

### Páginas Institucionais
- [x] Quem Somos
- [x] Principais Clientes (9 logos)
- [x] Contato (formulário + mapa)

### SEO & Performance
- [x] Meta tags otimizadas
- [x] Open Graph
- [x] Schema.org
- [x] Lazy loading de imagens
- [x] Código minificado (manual)
- [ ] Sitemap.xml
- [ ] Robots.txt
- [ ] Google Analytics

---

## 🚀 Próximos Passos / Melhorias Futuras

### Funcionalidades
1. **Sitemap XML:** Gerar sitemap.xml para SEO
2. **Robots.txt:** Criar arquivo robots.txt
3. **Google Analytics:** Integrar GA4
4. **Formulário Backend:** Integrar com sistema de envio de e-mail real (PHP, Node.js, ou serviço)
5. **WhatsApp Button:** Botão flutuante de WhatsApp
6. **Chat ao Vivo:** Integração com Tawk.to ou similar
7. **Blog:** Seção de notícias/artigos
8. **Portfólio:** Galeria expandida de projetos

### Performance
1. **Minificação:** Minificar CSS/JS
2. **Compressão:** Otimizar imagens (WebP)
3. **CDN:** Configurar CDN para assets
4. **Caching:** Headers de cache no servidor
5. **Service Worker:** PWA para funcionamento offline

### SEO
1. **Breadcrumbs Schema:** Adicionar structured data para breadcrumbs
2. **Local Business Schema:** Schema específico para empresas locais
3. **Reviews Schema:** Schema para avaliações de clientes
4. **Canonical URLs:** Tags canonical em todas as páginas
5. **Hreflang:** Se houver versão em inglês

### Acessibilidade (A11y)
1. **ARIA Labels:** Melhorar labels para screen readers
2. **Contraste:** Verificar contraste de cores (WCAG AA)
3. **Focus Visible:** Melhorar indicadores de foco
4. **Skip Links:** Links para pular navegação
5. **Alt Text:** Revisar todos os alt texts

### Mobile
1. **Touch Gestures:** Melhorar gestos touch no slider
2. **Menu Mobile:** Animação mais suave
3. **Fonts Mobile:** Ajustar tamanhos de fonte
4. **Click Areas:** Aumentar áreas de toque

---

## 🔍 Como Testar

### Servidor Local
```bash
# Opção 1: Python
cd /home/luiz-ricardo/projects/safeoffshore
python3 -m http.server 8000

# Opção 2: Node.js
npx http-server -p 8000

# Opção 3: PHP
php -S localhost:8000
```

**URL:** http://localhost:8000

### Testar Responsividade
1. Chrome DevTools (F12)
2. Testar breakpoints: 320px, 768px, 992px, 1200px
3. Testar orientação portrait/landscape

### Testar Funcionalidades
- [ ] Slider funciona (setas, dots, teclado, touch)
- [ ] Menu mobile abre/fecha
- [ ] Modal de imagens funciona
- [ ] Formulário abre e-mail
- [ ] Links de telefone funcionam (mobile)
- [ ] Mapa carrega corretamente
- [ ] Back to top funciona
- [ ] Smooth scroll funciona

---

## 📝 Observações Importantes

### Nomenclatura de Arquivos
**TODOS os arquivos de imagem seguem o padrão `*82b7.*`**

Se uma imagem não carregar, verificar:
1. Nome do arquivo tem o sufixo `82b7`?
2. Caminho está correto? (`attachments/Image/` ou `attachments/Slider/`)
3. Extensão está correta? (jpg, png, gif)

### Estrutura de Páginas
Todas as páginas seguem o padrão:
```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <!-- Meta tags, title, links -->
</head>
<body>
    <header class="header" id="header">...</header>
    <section class="page-header">...</section>
    <section class="main-content">...</section>
    <footer class="footer">...</footer>
    <button class="back-to-top">...</button>
    <script src="../js/modern-script.js"></script>
</body>
</html>
```

### CSS Classes Globais
- `.container`: Sempre usar para conteúdo centralizado
- `.section-header`: Para títulos de seção
- `.btn-primary` / `.btn-secondary`: Botões padrão
- `.active`: Marca item ativo no menu

### JavaScript Events
Todos inicializados no final de `modern-script.js`:
```javascript
// Auto-initialize on DOMContentLoaded
initMobileMenu();
initHeroSlider();
initBackToTop();
initGalleryModal();
initSmoothScroll();
initHeaderScroll();
animateOnScroll();
initContactForm();
```

---

## 📞 Informações da Empresa (Referência)

**Razão Social:** SAFE OFFSHORE Serviços Marítimos Ltda.

**Endereço:**
Rua Fortunato Abreu Gágno, 728, Sala 1
Jardim Camburi, Vitória - ES
CEP: 29090-200

**Contatos:**
- Tel: (27) 3376-4732
- Cel: (27) 9.9620-7455 (Alcântara)
- Cel: (27) 9.9740-7072 (Rhoger)
- E-mail: contato@safeoffshore.com.br

**Horário:**
- Segunda a Sexta: 08:00 - 18:00
- Sábado: 08:00 - 12:00

**Certificações:**
- CAMR (Centro de Sinalização Náutica Almirante Moraes Rego)
- IRATA (Industrial Rope Access Trade Association)

---

## 🎓 Padrões de Código

### HTML
- Usar semântica HTML5 (`<header>`, `<nav>`, `<section>`, `<article>`, `<footer>`)
- Indentação: 4 espaços
- Atributos em ordem: class, id, data-*, src, href, alt
- Alt text obrigatório em todas as imagens

### CSS
- Seguir ordem: Positioning, Box Model, Typography, Visual, Misc
- Usar variáveis CSS para cores/espaçamentos
- Mobile-first (media queries em ordem crescente)
- Evitar `!important` (usar especificidade correta)

### JavaScript
- ES6+ (const/let, arrow functions, template literals)
- Modular (uma função = uma responsabilidade)
- Event delegation quando possível
- Comentários JSDoc para funções complexas

---

## 📊 Estatísticas do Projeto

- **Páginas HTML:** 12
- **Linhas CSS:** ~1470
- **Linhas JS:** ~512
- **Imagens:** 40+
- **Logos de Clientes:** 9
- **Serviços:** 6
- **Breakpoints:** 3 (768px, 992px, 1200px)

---

## 🔗 Links Úteis

- **CAMR:** https://www.mar.mil.br/dhn/camr/camr.html
- **Praticagem:** http://www.praticagem.org.br/
- **Font Awesome:** https://fontawesome.com/
- **Google Fonts:** https://fonts.google.com/

---

## 📅 Histórico de Alterações

### Outubro 2024
- ✅ Criação do site moderno (HTML5 + CSS3 + JS Vanilla)
- ✅ Implementação de todas as páginas
- ✅ Integração de todas as imagens
- ✅ Formulário de contato funcional
- ✅ SEO básico implementado
- ✅ Responsividade completa
- ✅ Gallery modal com zoom
- ✅ Correção do mapa do Google Maps
- ✅ Documentação completa

---

## 👨‍💻 Para o Desenvolvedor Futuro

Quando voltar a este projeto:

1. **Leia este arquivo primeiro** para entender a estrutura
2. **Verifique o padrão `82b7`** em nomes de arquivos de imagem
3. **Use o servidor local** (não abra arquivos diretamente)
4. **Teste em múltiplos dispositivos** antes de fazer deploy
5. **Mantenha o padrão de código** estabelecido
6. **Documente novas funcionalidades** neste arquivo

### Comandos Rápidos
```bash
# Iniciar servidor
cd /home/luiz-ricardo/projects/safeoffshore
python3 -m http.server 8000

# Procurar por TODO no código
grep -r "TODO" .

# Listar todas as imagens
find attachments/ -name "*82b7.*"

# Validar HTML
# Use: https://validator.w3.org/

# Minificar CSS
# Use: https://cssminifier.com/

# Minificar JS
# Use: https://javascript-minifier.com/
```

---

**Última Atualização:** Outubro 2024
**Versão da Documentação:** 1.0
**Desenvolvido por:** Claude Code (Anthropic)

---

*Esta documentação deve ser atualizada sempre que houver mudanças significativas no projeto.*
