/* ========================================
   Safe Offshore - Modern JavaScript
   ======================================== */

/* ========== WebP Fallback ========== */
// Se o servidor não entregar a versão .webp de um <picture> (ex.: IIS sem o
// MIME registrado), remove o <source> para o navegador usar o <img src>.
function useImageFallback(img) {
    const picture = img.parentElement;
    if (!picture || picture.tagName !== 'PICTURE' || !picture.querySelector('source')) return;
    picture.querySelectorAll('source').forEach(source => source.remove());
    img.src = img.getAttribute('src');
}

document.addEventListener('error', function(e) {
    if (e.target.tagName === 'IMG') useImageFallback(e.target);
}, true);

document.querySelectorAll('picture > img').forEach(img => {
    if (img.complete && img.naturalWidth === 0 && img.currentSrc) useImageFallback(img);
});

/* ========== Analytics: cliques de contato ========== */
// Registra no GA4 os contatos iniciados (WhatsApp, telefone, e-mail); nada acontece sem o gtag.
function trackContact(method, location) {
    if (typeof gtag === 'function') gtag('event', 'contato', { metodo: method, local: location });
}

document.addEventListener('click', function(e) {
    const link = e.target.closest('a[href]');
    if (!link) return;
    const href = link.getAttribute('href');
    const location = link.classList.contains('whatsapp-float') ? 'botao_flutuante' : (link.closest('footer') ? 'rodape' : 'pagina');
    if (href.includes('wa.me/')) trackContact('whatsapp', location);
    else if (href.startsWith('tel:')) trackContact('telefone', location);
    else if (href.startsWith('mailto:')) trackContact('email', location);
});

// DOM Ready
document.addEventListener('DOMContentLoaded', function() {
    initMobileMenu();
    initHeroSlider();
    initBackToTop();
    initGalleryModal();
    initSmoothScroll();
    initHeaderScroll();
    initDropdownMobile();
    initCookieConsent();
});

/* ========== Idioma ========== */
// Textos gerados pelo script seguem o idioma da página (<html lang="en"> nas páginas em /en/).
const LANG_EN = document.documentElement.lang === 'en';
const TEXTS = LANG_EN ? {
    cookiePrefs: 'Cookie preferences',
    cookieLabel: 'Cookie notice',
    cookieText: 'We use Google Analytics cookies to understand how the site is used and improve it. They are only enabled if you accept.',
    accept: 'Accept',
    decline: 'Decline',
    quoteGreeting: 'Hello! I would like to request a quote.',
    name: 'Name', company: 'Company', phone: 'Phone', service: 'Service',
    quoteSubject: 'Quote request'
} : {
    cookiePrefs: 'Preferências de cookies',
    cookieLabel: 'Aviso de cookies',
    cookieText: 'Usamos cookies do Google Analytics para entender como o site é usado e melhorá-lo. Eles só são ativados se você aceitar.',
    accept: 'Aceitar',
    decline: 'Recusar',
    quoteGreeting: 'Olá! Gostaria de solicitar um orçamento.',
    name: 'Nome', company: 'Empresa', phone: 'Telefone', service: 'Serviço',
    quoteSubject: 'Orçamento'
};

/* ========== Aviso de cookies (LGPD) ========== */
// O Analytics só é carregado depois do "Aceitar" (ver carregarAnalytics() no <head>).
const CONSENT_KEY = 'cookies-consentimento';

function getConsent() {
    try { return localStorage.getItem(CONSENT_KEY); } catch (e) { return null; }
}

function setConsent(value) {
    try { localStorage.setItem(CONSENT_KEY, value); } catch (e) {}
}

function initCookieConsent() {
    const footerBottom = document.querySelector('.footer-bottom');
    if (footerBottom) {
        const prefs = document.createElement('button');
        prefs.type = 'button';
        prefs.className = 'cookie-prefs-link';
        prefs.textContent = TEXTS.cookiePrefs;
        prefs.addEventListener('click', showCookieBanner);
        footerBottom.appendChild(prefs);
    }
    if (!getConsent()) showCookieBanner();
}

function showCookieBanner() {
    if (document.getElementById('cookieBanner')) return;
    const banner = document.createElement('div');
    banner.id = 'cookieBanner';
    banner.className = 'cookie-banner';
    banner.setAttribute('role', 'region');
    banner.setAttribute('aria-label', TEXTS.cookieLabel);
    banner.innerHTML = `
        <p>${TEXTS.cookieText}</p>
        <div class="cookie-banner-actions">
            <button type="button" class="btn btn-primary" data-consent="aceito">${TEXTS.accept}</button>
            <button type="button" class="btn btn-outline-light" data-consent="recusado">${TEXTS.decline}</button>
        </div>`;
    banner.addEventListener('click', function(e) {
        const choice = e.target.closest('[data-consent]');
        if (!choice) return;
        const previous = getConsent();
        setConsent(choice.dataset.consent);
        banner.remove();
        if (choice.dataset.consent === 'aceito' && previous !== 'aceito' && typeof carregarAnalytics === 'function') {
            carregarAnalytics();
        } else if (choice.dataset.consent === 'recusado' && previous === 'aceito') {
            window.location.reload(); // descarrega o Analytics que já estava ativo
        }
    });
    document.body.appendChild(banner);
}

/* ========== Mobile Menu ========== */
function initMobileMenu() {
    const mobileMenuToggle = document.getElementById('mobileMenuToggle');
    const navMenu = document.getElementById('navMenu');

    if (mobileMenuToggle && navMenu) {
        mobileMenuToggle.addEventListener('click', function() {
            navMenu.classList.toggle('active');
            this.classList.toggle('active');

            // Animate hamburger
            const spans = this.querySelectorAll('span');
            if (this.classList.contains('active')) {
                spans[0].style.transform = 'rotate(45deg) translate(5px, 5px)';
                spans[1].style.opacity = '0';
                spans[2].style.transform = 'rotate(-45deg) translate(7px, -6px)';
            } else {
                spans[0].style.transform = '';
                spans[1].style.opacity = '';
                spans[2].style.transform = '';
            }
        });

        // Close menu when clicking on a link (but not dropdown toggle)
        const navLinks = navMenu.querySelectorAll('a:not(.dropdown-toggle)');
        navLinks.forEach(link => {
            link.addEventListener('click', function() {
                if (window.innerWidth <= 768) {
                    navMenu.classList.remove('active');
                    mobileMenuToggle.classList.remove('active');
                    const spans = mobileMenuToggle.querySelectorAll('span');
                    spans[0].style.transform = '';
                    spans[1].style.opacity = '';
                    spans[2].style.transform = '';
                }
            });
        });

        // Close menu when clicking outside
        document.addEventListener('click', function(event) {
            if (!navMenu.contains(event.target) && !mobileMenuToggle.contains(event.target)) {
                navMenu.classList.remove('active');
                mobileMenuToggle.classList.remove('active');
                const spans = mobileMenuToggle.querySelectorAll('span');
                spans[0].style.transform = '';
                spans[1].style.opacity = '';
                spans[2].style.transform = '';
            }
        });
    }
}

/* ========== Dropdown Mobile ========== */
function initDropdownMobile() {
    const dropdowns = document.querySelectorAll('.dropdown');

    dropdowns.forEach(dropdown => {
        const toggle = dropdown.querySelector('.dropdown-toggle');

        if (toggle) {
            toggle.addEventListener('click', function(e) {
                // Check if mobile menu is visible (better than window.innerWidth)
                const mobileMenuToggle = document.getElementById('mobileMenuToggle');
                const isMobile = mobileMenuToggle && window.getComputedStyle(mobileMenuToggle).display !== 'none';

                if (isMobile) {
                    e.preventDefault();
                    e.stopPropagation();

                    // Close other dropdowns
                    dropdowns.forEach(otherDropdown => {
                        if (otherDropdown !== dropdown) {
                            otherDropdown.classList.remove('active');
                        }
                    });

                    // Toggle current dropdown
                    dropdown.classList.toggle('active');
                }
            });
        }
    });

    // Close dropdown when clicking outside (only on mobile)
    document.addEventListener('click', function(e) {
        const mobileMenuToggle = document.getElementById('mobileMenuToggle');
        const isMobile = mobileMenuToggle && window.getComputedStyle(mobileMenuToggle).display !== 'none';

        if (isMobile && !e.target.closest('.dropdown')) {
            dropdowns.forEach(dropdown => {
                dropdown.classList.remove('active');
            });
        }
    });
}

/* ========== Hero Slider ========== */
function initHeroSlider() {
    const slides = document.querySelectorAll('.slide');
    const prevBtn = document.getElementById('prevSlide');
    const nextBtn = document.getElementById('nextSlide');
    const dotsContainer = document.getElementById('sliderDots');

    if (slides.length === 0) return;

    let currentSlide = 0;
    let slideInterval;

    // Create dots
    slides.forEach((_, index) => {
        const dot = document.createElement('div');
        dot.classList.add('dot');
        if (index === 0) dot.classList.add('active');
        dot.addEventListener('click', () => goToSlide(index));
        dotsContainer.appendChild(dot);
    });

    const dots = document.querySelectorAll('.dot');

    function showSlide(n) {
        slides.forEach(slide => slide.classList.remove('active'));
        dots.forEach(dot => dot.classList.remove('active'));

        currentSlide = (n + slides.length) % slides.length;

        slides[currentSlide].classList.add('active');
        dots[currentSlide].classList.add('active');
    }

    function nextSlide() {
        showSlide(currentSlide + 1);
    }

    function prevSlide() {
        showSlide(currentSlide - 1);
    }

    function goToSlide(n) {
        showSlide(n);
        resetInterval();
    }

    function startInterval() {
        slideInterval = setInterval(nextSlide, 5000);
    }

    function resetInterval() {
        clearInterval(slideInterval);
        startInterval();
    }

    // Event listeners
    if (prevBtn) prevBtn.addEventListener('click', () => {
        prevSlide();
        resetInterval();
    });

    if (nextBtn) nextBtn.addEventListener('click', () => {
        nextSlide();
        resetInterval();
    });

    // Keyboard navigation
    document.addEventListener('keydown', function(e) {
        if (e.key === 'ArrowLeft') {
            prevSlide();
            resetInterval();
        } else if (e.key === 'ArrowRight') {
            nextSlide();
            resetInterval();
        }
    });

    // Touch/Swipe support
    let touchStartX = 0;
    let touchEndX = 0;

    const heroSlider = document.getElementById('heroSlider');
    if (heroSlider) {
        heroSlider.addEventListener('touchstart', e => {
            touchStartX = e.changedTouches[0].screenX;
        });

        heroSlider.addEventListener('touchend', e => {
            touchEndX = e.changedTouches[0].screenX;
            handleSwipe();
        });

        function handleSwipe() {
            if (touchEndX < touchStartX - 50) {
                nextSlide();
                resetInterval();
            }
            if (touchEndX > touchStartX + 50) {
                prevSlide();
                resetInterval();
            }
        }
    }

    // Start auto-slide
    startInterval();

    // Pause on hover
    const hero = document.querySelector('.hero');
    if (hero) {
        hero.addEventListener('mouseenter', () => clearInterval(slideInterval));
        hero.addEventListener('mouseleave', startInterval);
    }
}

/* ========== Back to Top Button ========== */
function initBackToTop() {
    const backToTopBtn = document.getElementById('backToTop');

    if (backToTopBtn) {
        window.addEventListener('scroll', function() {
            if (window.pageYOffset > 300) {
                backToTopBtn.classList.add('show');
            } else {
                backToTopBtn.classList.remove('show');
            }
        });

        backToTopBtn.addEventListener('click', function() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }
}

/* ========== Gallery Modal ========== */
function initGalleryModal() {
    const galleryItems = document.querySelectorAll('.gallery-item, .service-image-item, .clickable-image');
    const modal = document.getElementById('galleryModal');
    const modalImage = document.getElementById('modalImage');
    const modalClose = document.getElementById('modalClose');
    const modalPrev = document.getElementById('modalPrev');
    const modalNext = document.getElementById('modalNext');

    if (!modal || galleryItems.length === 0) return;

    // Legenda da foto ampliada: a legenda visível (galeria, sinalização) ou o texto alternativo
    const modalCaption = document.createElement('p');
    modalCaption.className = 'modal-caption';
    modalCaption.id = 'modalCaption';
    modal.appendChild(modalCaption);

    let currentImageIndex = 0;
    const images = Array.from(galleryItems).map(item => {
        const img = item.tagName === 'IMG' ? item : item.querySelector('img');
        const visible = item.querySelector('figcaption, .operation-caption');
        const caption = visible ? visible.textContent : img.alt.replace(/\s*-\s*[^-]*Safe Offshore$/, '');
        return {
            src: img.src,
            alt: img.alt,
            caption: caption.trim()
        };
    });

    function openModal(index) {
        currentImageIndex = index;
        showImage();
        modal.classList.add('active');
        document.body.style.overflow = 'hidden';
    }

    function closeModal() {
        modal.classList.remove('active');
        document.body.style.overflow = '';
    }

    function showImage() {
        modalImage.src = images[currentImageIndex].src;
        modalImage.alt = images[currentImageIndex].alt;
        modalCaption.textContent = images[currentImageIndex].caption;
        modalCaption.hidden = !images[currentImageIndex].caption;
    }

    function nextImage() {
        currentImageIndex = (currentImageIndex + 1) % images.length;
        showImage();
    }

    function prevImage() {
        currentImageIndex = (currentImageIndex - 1 + images.length) % images.length;
        showImage();
    }

    // Event listeners
    galleryItems.forEach((item, index) => {
        item.style.cursor = 'pointer';
        item.addEventListener('click', () => openModal(index));
    });

    if (modalClose) {
        modalClose.addEventListener('click', closeModal);
    }

    if (modalPrev) {
        modalPrev.addEventListener('click', prevImage);
    }

    if (modalNext) {
        modalNext.addEventListener('click', nextImage);
    }

    // Close on background click
    modal.addEventListener('click', function(e) {
        if (e.target === modal) {
            closeModal();
        }
    });

    // Keyboard navigation
    document.addEventListener('keydown', function(e) {
        if (!modal.classList.contains('active')) return;

        if (e.key === 'Escape') {
            closeModal();
        } else if (e.key === 'ArrowLeft') {
            prevImage();
        } else if (e.key === 'ArrowRight') {
            nextImage();
        }
    });
}

/* ========== Smooth Scroll ========== */
function initSmoothScroll() {
    const links = document.querySelectorAll('a[href^="#"]');

    links.forEach(link => {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');

            // Ignore empty hash or just #
            if (href === '#' || href === '') return;

            const target = document.querySelector(href);

            if (target) {
                e.preventDefault();
                const headerOffset = 80;
                const elementPosition = target.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

                window.scrollTo({
                    top: offsetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
}

/* ========== Header Scroll Effect ========== */
function initHeaderScroll() {
    const header = document.getElementById('header');

    if (header) {
        window.addEventListener('scroll', function() {
            const currentScroll = window.pageYOffset;

            if (currentScroll > 100) {
                header.classList.add('scrolled');
            } else {
                header.classList.remove('scrolled');
            }
        });
    }
}

/* ========== Lazy Loading (Optional Enhancement) ========== */
if ('IntersectionObserver' in window) {
    const lazyImages = document.querySelectorAll('img[loading="lazy"]');

    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.src; // Trigger load
                img.classList.add('loaded');
                observer.unobserve(img);
            }
        });
    });

    lazyImages.forEach(img => imageObserver.observe(img));
}

/* ========== Animation on Scroll (Optional Enhancement) ========== */
function animateOnScroll() {
    const elements = document.querySelectorAll('.feature-card, .service-card, .gallery-item');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '0';
                entry.target.style.transform = 'translateY(20px)';

                setTimeout(() => {
                    entry.target.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }, 100);

                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1
    });

    elements.forEach(element => {
        observer.observe(element);
    });
}

// Initialize animation on scroll
if ('IntersectionObserver' in window) {
    animateOnScroll();
}

/* ========== Performance Optimization ========== */
// Debounce function for performance
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Optimize scroll events
window.addEventListener('scroll', debounce(function() {
    // Any additional scroll-based functionality
}, 10));

// Optimize resize events
window.addEventListener('resize', debounce(function() {
    // Close mobile menu on resize to desktop
    if (window.innerWidth > 768) {
        const navMenu = document.getElementById('navMenu');
        const mobileMenuToggle = document.getElementById('mobileMenuToggle');

        if (navMenu && navMenu.classList.contains('active')) {
            navMenu.classList.remove('active');
            mobileMenuToggle.classList.remove('active');
        }
    }
}, 250));

/* ========== Contact Form (orçamento via WhatsApp ou e-mail) ========== */
const CONTACT_WHATSAPP = '5527996207455';
const CONTACT_EMAIL = 'contato@safeoffshore.com.br';

function initContactForm() {
    const contactForm = document.getElementById('contactForm');
    if (!contactForm) return;

    let channel = 'whatsapp';
    contactForm.querySelectorAll('button[data-channel]').forEach(button => {
        button.addEventListener('click', function() {
            channel = this.dataset.channel;
        });
    });

    contactForm.addEventListener('submit', function(e) {
        e.preventDefault();

        let firstInvalid = null;
        contactForm.querySelectorAll('[required]').forEach(input => {
            const invalid = !input.value.trim();
            input.classList.toggle('error', invalid);
            input.setAttribute('aria-invalid', invalid);
            if (invalid && !firstInvalid) firstInvalid = input;
        });
        if (firstInvalid) {
            firstInvalid.focus();
            return;
        }

        const field = id => document.getElementById(id).value.trim();
        const lines = [
            TEXTS.quoteGreeting,
            '',
            `${TEXTS.name}: ${field('name')}`,
            field('company') ? `${TEXTS.company}: ${field('company')}` : null,
            `${TEXTS.phone}: ${field('phone')}`,
            field('service') ? `${TEXTS.service}: ${field('service')}` : null,
            '',
            field('message')
        ];
        const text = lines.filter(line => line !== null).join('\n');

        trackContact(channel === 'email' ? 'email' : 'whatsapp', 'formulario_orcamento');

        if (channel === 'email') {
            const subject = `${TEXTS.quoteSubject}${field('service') ? ' - ' + field('service') : ''} (site)`;
            window.location.href = `mailto:${CONTACT_EMAIL}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(text)}`;
        } else {
            window.open(`https://wa.me/${CONTACT_WHATSAPP}?text=${encodeURIComponent(text)}`, '_blank', 'noopener');
        }
    });

    contactForm.addEventListener('input', function(e) {
        if (e.target.value.trim()) {
            e.target.classList.remove('error');
            e.target.removeAttribute('aria-invalid');
        }
    });
}

// Initialize contact form
initContactForm();

/* ========== Console Message ========== */
console.log('%c🌊 Safe Offshore - Serviços Marítimos', 'color: #1a3657; font-size: 20px; font-weight: bold;');
console.log('%cSite desenvolvido com tecnologias modernas para melhor experiência do usuário.', 'color: #cf651f; font-size: 12px;');
