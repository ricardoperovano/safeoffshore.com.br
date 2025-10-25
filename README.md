# Safe Offshore - Website Moderno

Site institucional da Safe Offshore Serviços Marítimos, completamente renovado com tecnologias web modernas.

## 🚀 Melhorias Implementadas

### ✨ Design Moderno e Responsivo
- **Layout Clean e Profissional**: Design totalmente reformulado com foco em usabilidade
- **Responsivo**: Funciona perfeitamente em desktops, tablets e smartphones
- **Navegação Intuitiva**: Menu mobile com hamburguer animado
- **Hero Slider**: Carrossel automático de imagens com controles e indicadores
- **Animações Suaves**: Transições e efeitos modernos que melhoram a experiência do usuário

### 🎨 Recursos Visuais
- **Paleta de Cores Profissional**: Azuis náuticos que refletem o setor marítimo
- **Tipografia Moderna**: Google Fonts (Poppins e Roboto)
- **Ícones Font Awesome**: Ícones vetoriais escaláveis
- **Cards Interativos**: Efeitos hover em serviços e features
- **Galeria de Imagens**: Modal lightbox para visualização ampliada
- **Gradientes e Sombras**: Efeitos visuais modernos

### 🔍 Otimização SEO
- **Meta Tags Completas**: Title, description, keywords otimizados
- **Open Graph**: Compartilhamento otimizado em redes sociais
- **Twitter Cards**: Preview adequado no Twitter
- **Structured Data**: Schema.org para melhor indexação
- **Semântica HTML5**: Tags semânticas corretas
- **Alt Text**: Todas as imagens com textos alternativos
- **URLs Amigáveis**: Estrutura de links clara
- **Performance**: Lazy loading de imagens

### ⚡ Performance
- **CSS Moderno**: Variáveis CSS, Grid e Flexbox
- **JavaScript Otimizado**: Debounce em eventos de scroll/resize
- **Lazy Loading**: Carregamento sob demanda de imagens
- **Preconnect**: Conexão antecipada com fontes do Google
- **Código Limpo**: HTML, CSS e JS bem estruturados

### 📱 Funcionalidades Interativas
1. **Menu Responsivo**: Hamburguer menu para mobile
2. **Hero Slider Automático**: Com controles manual, teclado e touch
3. **Galeria Modal**: Visualização ampliada com navegação
4. **Scroll Suave**: Navegação fluida entre seções
5. **Botão "Voltar ao Topo"**: Aparece ao rolar a página
6. **Dropdown Menus**: Submenu de serviços
7. **Animações ao Rolar**: Elementos aparecem suavemente

## 📁 Estrutura de Arquivos

```
safeoffshore/
├── index.html              # Página principal renovada
├── css/
│   └── modern-style.css    # Estilos modernos e responsivos
├── js/
│   └── modern-script.js    # JavaScript para interatividade
├── attachments/            # Imagens e recursos
├── about-us/               # Página "Quem Somos"
├── servicos/               # Páginas de serviços
├── contato/                # Página de contato
└── README.md              # Este arquivo
```

## 🎯 Recursos Principais

### Header/Navegação
- Logo clicável
- Menu responsivo com dropdown
- Efeito de scroll no header
- Menu mobile totalmente funcional

### Hero Section
- Slider automático de 5 imagens
- Controles de navegação (setas e dots)
- Suporte a teclado (← →) e touch (swipe)
- Overlay com gradiente
- Call-to-actions destacados

### Seção Sobre
- Texto institucional
- 4 features com ícones:
  - Experiência
  - Segurança
  - Meio Ambiente
  - Qualidade

### Seção Serviços
- Grid de 6 serviços principais
- Cards com hover effects
- Links para páginas detalhadas

### Galeria
- Grid responsivo de imagens
- Modal lightbox
- Navegação entre imagens
- Suporte a teclado (ESC, ← →)

### Links Importantes
- Grid de parceiros/certificações
- Links externos com segurança (rel="noopener noreferrer")

### Footer
- 4 colunas informativas
- Links rápidos
- Informações de contato
- Copyright atualizado

## 🌐 Navegadores Suportados
- Chrome (últimas 2 versões)
- Firefox (últimas 2 versões)
- Safari (últimas 2 versões)
- Edge (últimas 2 versões)
- Navegadores mobile modernos

## 📱 Breakpoints Responsivos
- Desktop: > 992px
- Tablet: 768px - 992px
- Mobile: < 768px
- Small Mobile: < 480px

## 🎨 Paleta de Cores
- **Azul Primário**: #0066cc
- **Azul Escuro**: #004999
- **Azul Secundário**: #00a8e8
- **Laranja Accent**: #ff6b35
- **Azul Marinho**: #003d5b
- **Texto**: #2c3e50

## ⚙️ Tecnologias Utilizadas
- HTML5 semântico
- CSS3 (Grid, Flexbox, Custom Properties)
- JavaScript ES6+ (Vanilla)
- Google Fonts (Poppins, Roboto)
- Font Awesome 6.4.0

## 🚀 Como Usar

1. **Abra o index.html** no navegador
2. **Navegue** pelo menu para explorar as seções
3. **No mobile**, clique no ícone de hamburguer para abrir o menu
4. **No hero slider**, use as setas ou arraste para mudar slides
5. **Na galeria**, clique nas imagens para ampliar

## ✅ Páginas Implementadas

- ✅ Homepage (index.html)
- ✅ Quem Somos (about-us/)
- ✅ Serviços - Página Principal (servicos/)
- ✅ Sinalização Náutica (servicos/sinalizacao-nautica/) - 7 imagens
- ✅ Comércio de Equipamentos (servicos/comercio-de-equipamentos-de-sinalizacao-nautica/) - 2 imagens
- ✅ Apoio Subaquático (servicos/apoio-subaquatico/) - 4 imagens
- ✅ Agulha Magnética (servicos/agulha-magnetica-e-barometro-aneroide/) - 3 imagens
- ✅ Hidrelétricas (servicos/hidreletricas/) - 3 imagens
- ✅ Alpinismo Industrial (servicos/alpinismo-industrial/) - 3 imagens
- ✅ Principais Clientes (principais-clientes-1/) - 9 logos
- ✅ Contato (contato/) - Formulário + Mapa

## 🔧 Servidor Local

```bash
cd /home/luiz-ricardo/projects/safeoffshore
python3 -m http.server 8000
# Acesse: http://localhost:8000
```

**⚠️ IMPORTANTE:** Não abra os arquivos HTML diretamente no navegador (file://). Use um servidor local para evitar problemas de CORS com fontes e recursos externos.

## ⚠️ Padrão de Nomenclatura de Imagens

**TODOS os arquivos de imagem seguem o padrão `*82b7.*`**

Exemplos:
- `IRATA82b7.jpg` ✅
- `technip82b7.jpg` ✅
- `Imagem382b7.png` ✅

Se uma imagem não carregar, verifique se o nome tem o sufixo `82b7`.

## 📝 Próximos Passos

- [ ] Sitemap.xml para SEO
- [ ] Robots.txt
- [ ] Google Analytics / GA4
- [ ] Minificação CSS/JS para produção
- [ ] Otimização de imagens (converter para WebP)
- [ ] Backend real para formulário de contato
- [ ] WhatsApp Button flutuante
- [ ] Sistema de blog/notícias
- [ ] Área administrativa
- [ ] Multi-idioma (PT/EN)

## 📧 Contato da Empresa

**Safe Offshore Serviços Marítimos**
- 📍 Rua Fortunato Abreu Gágno, 728, Sala 1, Jardim Camburi, Vitória - ES, CEP: 29090-200
- ☎️ (27) 3376-4732
- 📱 (27) 9.9620-7455 (Alcântara)
- 📱 (27) 9.9740-7072 (Rhoger)
- 📧 contato@safeoffshore.com.br
- 🌐 www.safeoffshore.com.br

## 📚 Documentação Completa

Para informações técnicas detalhadas, estrutura de código e padrões, consulte:
**[DOCUMENTACAO.md](./DOCUMENTACAO.md)**

---

© 2015-2024 SAFE OFFSHORE Serviços Marítimos Ltda. Todos os Direitos Reservados.
