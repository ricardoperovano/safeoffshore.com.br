# Quick Reference - Safe Offshore

Guia rápido de referência para desenvolvimento e manutenção do site.

---

## 🚀 Comandos Rápidos

### Iniciar Servidor Local
```bash
cd /home/luiz-ricardo/projects/safeoffshore
python3 -m http.server 8000
```
**URL:** http://localhost:8000

### Buscar no Código
```bash
# Procurar por classe CSS
grep -r "class-name" css/

# Procurar por função JS
grep -r "function-name" js/

# Procurar TODO/FIXME
grep -r "TODO\|FIXME" .

# Listar todas as imagens
find attachments/ -name "*82b7.*"
```

---

## 📁 Estrutura de Arquivos

```
safeoffshore/
├── index.html                    # Homepage
├── about-us/index.html           # Quem Somos
├── servicos/
│   ├── index.html                # Listagem de Serviços
│   ├── sinalizacao-nautica/
│   ├── alpinismo-industrial/
│   ├── apoio-subaquatico/
│   ├── agulha-magnetica-e-barometro-aneroide/
│   ├── hidreletricas/
│   └── comercio-de-equipamentos-de-sinalizacao-nautica/
├── principais-clientes-1/        # Clientes
├── contato/                      # Contato
├── css/modern-style.css          # CSS principal (1470+ linhas)
├── js/modern-script.js           # JS principal (512 linhas)
└── attachments/                  # Imagens
    ├── Image/                    # Imagens gerais
    ├── Logo/                     # Logos
    └── Slider/                   # Imagens de sliders
```

---

## 🎨 Classes CSS Importantes

### Layout
```css
.container              /* Max-width: 1200px, centralizado */
.section-header         /* Cabeçalho de seção */
.section-title          /* Título com underline */
.title-underline        /* Linha decorativa */
```

### Componentes
```css
.service-card           /* Card de serviço */
.feature-card           /* Card de feature */
.client-item            /* Logo de cliente */
.contact-info-item      /* Card de contato */
.service-image-item     /* Container de imagem */
.gallery-item           /* Item de galeria */
```

### Botões
```css
.btn                    /* Botão base */
.btn-primary            /* Botão azul */
.btn-secondary          /* Botão cinza */
```

### Estados
```css
.active                 /* Item ativo no menu */
.scrolled               /* Header após scroll */
.error                  /* Input com erro */
```

### Imagens
```css
.clickable-image        /* Imagem clicável para zoom */
.service-images-grid    /* Grid de imagens */
```

---

## 🎯 Variáveis CSS

### Cores
```css
--primary-color: #1a5490;       /* Azul marinho */
--secondary-color: #00a8e8;     /* Azul claro */
--accent-color: #ff6b35;        /* Laranja */
--text-dark: #2c3e50;
--text-gray: #7f8c8d;
--text-light: #ffffff;
--bg-white: #ffffff;
--bg-light: #f8f9fa;
```

### Espaçamentos
```css
--spacing-xs: 0.5rem;           /* 8px */
--spacing-sm: 1rem;             /* 16px */
--spacing-md: 1.5rem;           /* 24px */
--spacing-lg: 2rem;             /* 32px */
--spacing-xl: 3rem;             /* 48px */
```

### Sombras
```css
--shadow-sm: 0 2px 4px rgba(0,0,0,0.1);
--shadow-md: 0 4px 6px rgba(0,0,0,0.1);
--shadow-lg: 0 8px 15px rgba(0,0,0,0.15);
```

---

## 📱 Breakpoints

```css
/* Mobile */
@media (max-width: 768px) { }

/* Tablet */
@media (min-width: 769px) and (max-width: 992px) { }

/* Desktop */
@media (min-width: 993px) { }
```

---

## 🔧 Funções JavaScript

### Principais Funções
```javascript
initMobileMenu()        // Menu hamburger
initHeroSlider()        // Slider automático
initBackToTop()         // Botão voltar ao topo
initGalleryModal()      // Modal de imagens
initSmoothScroll()      // Scroll suave
initHeaderScroll()      // Header no scroll
initContactForm()       // Formulário de contato
animateOnScroll()       // Animações ao rolar
```

### Modificar Slider
```javascript
// Trocar tempo de auto-play (padrão: 5000ms)
const slideInterval = setInterval(nextSlide, 5000); // ← Mudar aqui
```

### Adicionar Imagem ao Modal
```html
<!-- Adicionar classe para zoom -->
<img src="caminho/imagem82b7.jpg" class="clickable-image" alt="Descrição">

<!-- OU usar dentro de service-image-item -->
<div class="service-image-item">
    <img src="caminho/imagem82b7.jpg" alt="Descrição">
</div>
```

---

## 🖼️ Padrão de Nomenclatura de Imagens

**REGRA:** Todos os arquivos têm sufixo `82b7`

### Exemplos Corretos ✅
```
IRATA82b7.jpg
technip82b7.jpg
Imagem382b7.png
certificado82b7.png
linhapamarela82b7.png
```

### Exemplos Incorretos ❌
```
IRATA.jpg
technip.jpg
Imagem3.png
```

### Caminhos Comuns
```
attachments/Image/nome82b7.ext          # Imagens gerais
attachments/Logo/LOGO-01T-PNG.png       # Logo principal
attachments/Slider/[uuid]/nome82b7.ext  # Imagens de trabalhos
```

---

## 📄 Template de Página

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Título da Página - Safe Offshore</title>
    <meta name="description" content="Descrição da página">
    <link rel="icon" type="image/png" href="../attachments/Logo/LOGO-01T-PNG.png">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&family=Roboto:wght@300;400;500;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="../css/modern-style.css">
</head>
<body>
    <header class="header" id="header">
        <!-- Copiar header de outra página -->
    </header>

    <section class="page-header">
        <div class="page-header-overlay"></div>
        <div class="container">
            <h1 class="page-title">Título da Página</h1>
            <nav class="breadcrumb">
                <a href="../index.html">Home</a>
                <span class="separator">/</span>
                <span class="current">Página Atual</span>
            </nav>
        </div>
    </section>

    <section class="main-content">
        <div class="container">
            <!-- Conteúdo aqui -->
        </div>
    </section>

    <footer class="footer">
        <!-- Copiar footer de outra página -->
    </footer>

    <button class="back-to-top" id="backToTop">
        <i class="fas fa-chevron-up"></i>
    </button>

    <script src="../js/modern-script.js"></script>
</body>
</html>
```

---

## 🎨 Template de Card de Serviço

```html
<div class="service-card">
    <div class="service-icon">
        <i class="fas fa-icon-name"></i>
    </div>
    <h3>Nome do Serviço</h3>
    <p>Descrição breve do serviço.</p>
    <a href="link-do-servico/" class="btn btn-primary">Saiba Mais</a>
</div>
```

---

## 🖼️ Template de Galeria de Imagens

```html
<h3>Galeria</h3>
<div class="service-images-grid">
    <div class="service-image-item">
        <img src="../attachments/Image/imagem182b7.jpg" alt="Descrição" loading="lazy">
    </div>
    <div class="service-image-item">
        <img src="../attachments/Image/imagem282b7.jpg" alt="Descrição" loading="lazy">
    </div>
    <!-- Mais imagens... -->
</div>

<!-- Adicionar modal ao final da página (antes do </footer>) -->
<div class="gallery-modal" id="galleryModal">
    <button class="modal-close" id="modalClose" aria-label="Fechar">
        <i class="fas fa-times"></i>
    </button>
    <button class="modal-prev" id="modalPrev" aria-label="Imagem anterior">
        <i class="fas fa-chevron-left"></i>
    </button>
    <button class="modal-next" id="modalNext" aria-label="Próxima imagem">
        <i class="fas fa-chevron-right"></i>
    </button>
    <img src="" alt="Imagem ampliada" id="modalImage">
</div>
```

---

## 📞 Informações da Empresa

### Contato
```
Telefone: (27) 3376-4732
Celular 1: (27) 9.9620-7455 (Alcântara)
Celular 2: (27) 9.9740-7072 (Rhoger)
E-mail: contato@safeoffshore.com.br
```

### Endereço
```
Rua Fortunato Abreu Gágno, 728, Sala 1
Jardim Camburi
Vitória - ES
CEP: 29090-200
```

### Links de Telefone (HTML)
```html
<a href="tel:+552733764732">(27) 3376-4732</a>
<a href="tel:+5527996207455">(27) 9.9620-7455</a>
<a href="tel:+5527997407072">(27) 9.9740-7072</a>
```

---

## 🔍 SEO - Meta Tags Template

```html
<!-- Basic Meta Tags -->
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="Descrição de 150-160 caracteres">
<meta name="keywords" content="palavra1, palavra2, palavra3">

<!-- Open Graph (Facebook) -->
<meta property="og:title" content="Título da Página - Safe Offshore">
<meta property="og:description" content="Descrição da página">
<meta property="og:image" content="URL da imagem">
<meta property="og:url" content="URL da página">
<meta property="og:type" content="website">

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Título da Página">
<meta name="twitter:description" content="Descrição da página">
<meta name="twitter:image" content="URL da imagem">
```

---

## 🐛 Troubleshooting

### Imagem não carrega
1. ✅ Verificar se tem sufixo `82b7`
2. ✅ Verificar caminho (relativo correto)
3. ✅ Verificar extensão (jpg, png, gif)
4. ✅ Checar console do navegador (F12)

### Header não diminui no scroll
1. ✅ Verificar se `initHeaderScroll()` está sendo chamado
2. ✅ Verificar se classe `.scrolled` existe no CSS
3. ✅ Limpar cache do navegador (Ctrl+Shift+R)

### Modal não abre
1. ✅ Verificar se elemento tem classe correta (`.gallery-item`, `.service-image-item`, ou `.clickable-image`)
2. ✅ Verificar se `<div id="galleryModal">` existe na página
3. ✅ Verificar se `initGalleryModal()` está sendo chamado
4. ✅ Verificar console para erros

### Menu mobile não funciona
1. ✅ Verificar se botão tem `id="mobileMenuToggle"`
2. ✅ Verificar se menu tem `id="navMenu"`
3. ✅ Verificar se `initMobileMenu()` está sendo chamado

### Formulário não envia
1. ✅ Verificar se form tem `id="contactForm"`
2. ✅ Verificar se campos têm os IDs corretos (name, email, phone, subject, message)
3. ✅ Verificar se `initContactForm()` está sendo chamado

---

## 📚 Recursos Úteis

### Validadores
- HTML: https://validator.w3.org/
- CSS: https://jigsaw.w3.org/css-validator/
- Lighthouse (Chrome DevTools): F12 → Lighthouse

### Otimização
- Minificar CSS: https://cssminifier.com/
- Minificar JS: https://javascript-minifier.com/
- Otimizar Imagens: https://tinypng.com/
- Converter para WebP: https://cloudconvert.com/

### Ferramentas de Desenvolvimento
- Chrome DevTools: F12
- Responsive Design Mode: Ctrl+Shift+M
- Network Tab: Verificar carregamento de recursos
- Console: Verificar erros JS

---

## 📝 Checklist de Deploy

- [ ] Testar todas as páginas
- [ ] Verificar responsividade (mobile, tablet, desktop)
- [ ] Testar formulário de contato
- [ ] Verificar todos os links
- [ ] Verificar carregamento de imagens
- [ ] Testar navegação
- [ ] Validar HTML
- [ ] Validar CSS
- [ ] Testar performance (Lighthouse)
- [ ] Minificar CSS/JS
- [ ] Otimizar imagens
- [ ] Configurar robots.txt
- [ ] Criar sitemap.xml
- [ ] Configurar Google Analytics

---

*Última Atualização: Outubro 2024*
