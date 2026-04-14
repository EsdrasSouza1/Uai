/* ============================================
   UAI TURISMO — script.js
   ============================================ */

document.addEventListener('DOMContentLoaded', function () {

  // =============================================
  // 1. HERO CAROUSEL
  // =============================================
  const track = document.getElementById('heroTrack');
  const dotsEl = document.getElementById('heroDots');
  const prevBtn = document.getElementById('heroPrev');
  const nextBtn = document.getElementById('heroNext');
  const slides = track ? track.querySelectorAll('.hero-carousel-slide') : [];

  if (track && slides.length > 0) {
    let current = 0;
    let timer;

    slides.forEach((_, i) => {
      const dot = document.createElement('button');
      dot.className = 'hero-dot' + (i === 0 ? ' active' : '');
      dot.setAttribute('aria-label', 'Slide ' + (i + 1));
      dot.addEventListener('click', () => goTo(i));
      dotsEl.appendChild(dot);
    });

    function goTo(index) {
      dotsEl.querySelectorAll('.hero-dot')[current].classList.remove('active');
      current = (index + slides.length) % slides.length;
      track.style.transform = `translateX(-${current * 100}%)`;
      dotsEl.querySelectorAll('.hero-dot')[current].classList.add('active');
      resetTimer();
    }

    function resetTimer() {
      clearInterval(timer);
      timer = setInterval(() => goTo(current + 1), 4500);
    }

    prevBtn.addEventListener('click', () => goTo(current - 1));
    nextBtn.addEventListener('click', () => goTo(current + 1));

    let touchStartX = 0;
    track.addEventListener('touchstart', e => { touchStartX = e.touches[0].clientX; }, { passive: true });
    track.addEventListener('touchend', e => {
      const diff = touchStartX - e.changedTouches[0].clientX;
      if (Math.abs(diff) > 40) goTo(diff > 0 ? current + 1 : current - 1);
    });

    resetTimer();
  }

  // =============================================
  // 2. NAVBAR — scroll + mobile
  // =============================================
  const nav = document.getElementById('nav');
  const navToggle = document.getElementById('navToggle');
  const navMenu = document.getElementById('navMenu');

  // Marca scroll para aplicar classe .scrolled
  window.addEventListener('scroll', () => {
    nav.classList.toggle('scrolled', window.scrollY > 60);
  }, { passive: true });

  // Toggle do menu hambúrguer — versão única e correta
  navToggle.addEventListener('click', () => {
    const isOpen = navMenu.classList.toggle('open');
    navToggle.classList.toggle('open', isOpen);
    navToggle.setAttribute('aria-expanded', isOpen);
    // Trava/libera o scroll da página
    document.body.style.overflow = isOpen ? 'hidden' : '';
    document.documentElement.style.overflow = isOpen ? 'hidden' : '';
    // Integração com Lenis (se carregado)
    try {
      if (typeof window._lenis !== 'undefined') {
        isOpen ? window._lenis.stop() : window._lenis.start();
      }
    } catch(e) {}
  });

  // Fechar menu ao clicar em qualquer link dentro dele
  navMenu.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      navMenu.classList.remove('open');
      navToggle.classList.remove('open');
      navToggle.setAttribute('aria-expanded', false);
      document.body.style.overflow = '';
      document.documentElement.style.overflow = '';
      try {
        if (typeof window._lenis !== 'undefined') window._lenis.start();
      } catch(e) {}
    });
  });

  // =============================================
  // 3. FAQ ACCORDION
  // =============================================
  const faqItems = document.querySelectorAll('.faq-item');

  faqItems.forEach(item => {
    const btn = item.querySelector('.faq-question');
    const answer = item.querySelector('.faq-answer');

    btn.addEventListener('click', () => {
      const isOpen = answer.classList.contains('open');

      // Fechar todos
      faqItems.forEach(other => {
        other.querySelector('.faq-question').setAttribute('aria-expanded', 'false');
        other.querySelector('.faq-answer').classList.remove('open');
      });

      // Abrir o clicado se estava fechado
      if (!isOpen) {
        btn.setAttribute('aria-expanded', 'true');
        answer.classList.add('open');
      }
    });
  });

  // =============================================
  // 4. REVEAL ON SCROLL
  // =============================================
  const revealTargets = document.querySelectorAll(
    '.destino-card, .diferencial-card, .cadastur-inner, .section-header, .gallery-header, .faq-item, .faq-cta, .reviews-placeholder'
  );

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
