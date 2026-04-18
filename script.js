/* ============================================
   UAI TURISMO — script.js
   ============================================ */

document.addEventListener('DOMContentLoaded', function () {

  // =============================================
  // 1. NAVBAR & MOBILE MENU (Unificado e Corrigido)
  // =============================================
  const nav = document.getElementById('nav');
  const navToggle = document.getElementById('navToggle');
  const navMenu = document.getElementById('navMenu');
  const body = document.body;
  const html = document.documentElement;

  if (navToggle && navMenu) {
    // Controle de Scroll da Navbar
    window.addEventListener('scroll', () => {
      nav.classList.toggle('scrolled', window.scrollY > 60);
    }, { passive: true });

    // Toggle do menu hambúrguer
    navToggle.addEventListener('click', function (e) {
      e.preventDefault();
      const isOpen = navMenu.classList.toggle('open');
      this.classList.toggle('open', isOpen);
      this.setAttribute('aria-expanded', isOpen);

      // Trava o scroll em qualquer parte do site (Fix para Imagem 2)
      if (isOpen) {
        body.style.overflow = 'hidden';
        html.style.overflow = 'hidden';
        try { if (window._lenis) window._lenis.stop(); } catch (e) { }
      } else {
        body.style.overflow = '';
        html.style.overflow = '';
        try { if (window._lenis) window._lenis.start(); } catch (e) { }
      }
    });

    // Fecha o menu ao clicar em qualquer link
    const navLinks = navMenu.querySelectorAll('a');
    navLinks.forEach(link => {
      link.addEventListener('click', () => {
        navToggle.classList.remove('open');
        navMenu.classList.remove('open');
        navToggle.setAttribute('aria-expanded', 'false');
        body.style.overflow = '';
        html.style.overflow = '';
        try { if (window._lenis) window._lenis.start(); } catch (e) { }
      });
    });
  }

  // =============================================
  // 2. HERO CAROUSEL
  // =============================================
  const track = document.getElementById('heroTrack');
  const dotsEl = document.getElementById('heroDots');
  const prevBtn = document.getElementById('heroPrev');
  const nextBtn = document.getElementById('heroNext');
  const slides = track ? track.querySelectorAll('.hero-carousel-slide') : [];

  if (track && slides.length > 0) {
    let current = 0;
    let timer;

    // Criar dots dinamicamente
    slides.forEach((_, i) => {
      const dot = document.createElement('button');
      dot.className = 'hero-dot' + (i === 0 ? ' active' : '');
      dot.setAttribute('aria-label', 'Slide ' + (i + 1));
      dot.addEventListener('click', () => goTo(i));
      if (dotsEl) dotsEl.appendChild(dot);
    });

    function goTo(index) {
      if (dotsEl) {
        const dots = dotsEl.querySelectorAll('.hero-dot');
        if (dots[current]) dots[current].classList.remove('active');
        current = (index + slides.length) % slides.length;
        track.style.transform = `translateX(-${current * 100}%)`;
        if (dots[current]) dots[current].classList.add('active');
      } else {
        current = (index + slides.length) % slides.length;
        track.style.transform = `translateX(-${current * 100}%)`;
      }
      resetTimer();
    }

    function resetTimer() {
      clearInterval(timer);
      timer = setInterval(() => goTo(current + 1), 4500);
    }

    if (prevBtn) prevBtn.addEventListener('click', () => goTo(current - 1));
    if (nextBtn) nextBtn.addEventListener('click', () => goTo(current + 1));

    // Touch swipe para mobile
    let touchStartX = 0;
    track.addEventListener('touchstart', e => { touchStartX = e.touches[0].clientX; }, { passive: true });
    track.addEventListener('touchend', e => {
      const diff = touchStartX - e.changedTouches[0].clientX;
      if (Math.abs(diff) > 40) goTo(diff > 0 ? current + 1 : current - 1);
    });

    resetTimer();
  }

  // =============================================
  // 3. FAQ ACCORDION
  // =============================================
  const faqItems = document.querySelectorAll('.faq-item');

  faqItems.forEach(item => {
    const btnFaq = item.querySelector('.faq-question');
    const answer = item.querySelector('.faq-answer');

    if (btnFaq && answer) {
      btnFaq.addEventListener('click', () => {
        const isOpen = answer.classList.contains('open');

        // Fechar todos antes de abrir o novo
        faqItems.forEach(other => {
          const otherBtn = other.querySelector('.faq-question');
          const otherAns = other.querySelector('.faq-answer');
          if (otherBtn) otherBtn.setAttribute('aria-expanded', 'false');
          if (otherAns) otherAns.classList.remove('open');
        });

        if (!isOpen) {
          btnFaq.setAttribute('aria-expanded', 'true');
          answer.classList.add('open');
        }
      });
    }
  });

  // =============================================
  // 4. REVEAL ON SCROLL
  // =============================================
  const revealTargets = document.querySelectorAll(
    '.destino-card, .diferencial-card, .cadastur-inner, .section-header, .gallery-header, .faq-item, .faq-cta, .reviews-placeholder'
  );

  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver(entries => {
      entries.forEach(e => {
        if (e.isIntersecting) {
          e.target.classList.add('revealed');
          observer.unobserve(e.target);
        }
      });
    }, { threshold: 0.10 });

    revealTargets.forEach(el => {
      el.classList.add('will-reveal');
      observer.observe(el);
    });
  }

  // =============================================
  // 5. SMOOTH SCROLL
  // =============================================
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const href = this.getAttribute('href');
      if (!href || href === '#') return;
      const target = document.querySelector(href);
      if (target) {
        e.preventDefault();
        window.scrollTo({
          top: target.getBoundingClientRect().top + window.scrollY - 80,
          behavior: 'smooth'
        });
      }
    });
  });

});