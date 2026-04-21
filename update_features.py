import glob
import re

for fpath in glob.glob('*.html'):
    with open(fpath, 'r', encoding='utf-8') as f:
        text = f.read()

    # 1. Update chatbot button size & notification text
    text = re.sub(r'width: 56px;\s*height: 56px;', 'width: 72px;\n            height: 72px;', text)
    text = text.replace('Oi! Posso te ajudar? 🌊', 'Duvida? clique em mim!')
    
    # Update notif position to match new button height
    text = text.replace('bottom: 158px;', 'bottom: 174px;')
    text = text.replace('bottom: 148px;', 'bottom: 164px;')
    text = re.sub(r'#uai-chat-btn img \{\s*width: 48px;\s*height: 48px;', '#uai-chat-btn img {\n                width: 60px;\n                height: 60px;', text)
    text = re.sub(r'#uai-chat-btn \{\s*right: 12px;\s*bottom: 90px;\s*width: 48px;\s*height: 48px;', '#uai-chat-btn {\n                right: 12px;\n                bottom: 90px;\n                width: 60px;\n                height: 60px;', text)

    # 2. Add Floating WhatsApp Button
    floating_wpp = """
    <!-- Floating WhatsApp Button -->
    <a href="https://wa.me/5581997484915?text=Olá!%20vim%20pelo%20site%20e%20tenho%20uma%20duvida!" class="floating-wpp" target="_blank" aria-label="Ir para o WhatsApp">
        <svg viewBox="0 0 24 24" fill="white" width="32" height="32">
            <path d="M12.01 2.011c-5.513 0-9.998 4.484-9.998 9.996 0 1.968.513 3.864 1.488 5.539L2 22l4.571-1.474c1.611.91 3.447 1.39 5.34 1.39 5.514 0 9.999-4.484 9.999-9.996S17.525 2.011 12.01 2.011zm5.289 14.475c-.223.633-1.282 1.157-1.782 1.206-.479.047-1.127.16-3.626-.874-2.999-1.242-4.908-4.321-5.056-4.52-.149-.199-1.206-1.606-1.206-3.064 0-1.458.745-2.179 1.01-2.46.265-.281.579-.348.775-.348.199 0 .399.006.579.014.187.009.431-.073.666.495.249.601.862 2.115.945 2.281.082.166.132.365.033.564-.099.199-.149.332-.298.498-.149.166-.316.365-.449.481-.148.134-.305.283-.131.581.173.298.775 1.282 1.666 2.074 1.147 1.018 2.117 1.332 2.415 1.482.298.149.481.133.664-.083.182-.216.795-.929.994-1.245.199-.316.398-.266.666-.166.265.101 1.691.797 1.99 946.299.149.48.232.745.349.467.243.682.223 1.258-.073z" />
        </svg>
    </a>
    """
    
    # Add floating button before closing body if not exists
    if 'class="floating-wpp"' not in text:
        text = text.replace('</body>', floating_wpp + '\n</body>')

    # Update style for the floating button
    wpp_css = """
    <style>
        .floating-wpp {
            position: fixed;
            bottom: 24px;
            left: 24px;
            width: 60px;
            height: 60px;
            background-color: #25D366;
            color: white;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 32px;
            box-shadow: 0 4px 14px rgba(37, 211, 102, 0.4);
            z-index: 1000;
            transition: transform 0.3s ease;
        }
        .floating-wpp:hover {
            transform: scale(1.1);
        }
        @media (max-width: 480px) {
            .floating-wpp {
                bottom: 16px;
                left: 16px;
                width: 50px;
                height: 50px;
            }
            .floating-wpp svg { padding: 4px; }
        }
    </style>
    """
    if '.floating-wpp {' not in text:
        if '</style>\n\n    <!-- Botão flutuante -->' in text:
            text = text.replace('</style>\n\n    <!-- Botão flutuante -->', wpp_css + '\n    <!-- Botão flutuante -->')
        else:
            text = text.replace('</head>', wpp_css + '\n</head>')

    # 3. Update RC3 Carousel JavaScript script to loop seamlessly
    old_carousel_js = """        function update() {
            var vis = getVis();
            var maxCur = Math.max(0, total - vis);
            if (cur > maxCur) cur = maxCur;
            var offset = cur * getCardW();
            track.style.transform = 'translateX(-' + offset + 'px)';
            if (prev) prev.disabled = cur <= 0;
            if (next) next.disabled = cur >= maxCur;
            updateDots();
        }

        function goTo(i) {
            var vis = getVis();
            var maxCur = Math.max(0, total - vis);
            cur = Math.max(0, Math.min(i, maxCur));
            update();
        }

        if (prev) prev.addEventListener('click', function () { goTo(cur - getVis()); });
        if (next) next.addEventListener('click', function () { goTo(cur + getVis()); });

        // Touch swipe
        var tx = 0;
        track.addEventListener('touchstart', function (e) { tx = e.touches[0].clientX; }, { passive: true });
        track.addEventListener('touchend', function (e) {
            var d = tx - e.changedTouches[0].clientX;
            if (Math.abs(d) > 50) goTo(d > 0 ? cur + getVis() : cur - getVis());
        });

        window.addEventListener('resize', function () {
            buildDots();
            update();
        });

        buildDots();
        update();
    })();
</script>"""

    new_carousel_js = """        function update() {
            var offset = cur * getCardW();
            track.style.transform = 'translateX(-' + offset + 'px)';
            if (prev) prev.disabled = false;
            if (next) next.disabled = false;
            updateDots();
        }

        function goTo(i) {
            var vis = getVis();
            var maxCur = Math.max(0, total - vis);
            if (i > maxCur) i = 0;
            if (i < 0) i = maxCur;
            cur = i;
            update();
        }

        if (prev) prev.addEventListener('click', function () { goTo(cur - 1); });
        if (next) next.addEventListener('click', function () { goTo(cur + 1); });

        // Touch swipe
        var tx = 0;
        track.addEventListener('touchstart', function (e) { tx = e.touches[0].clientX; }, { passive: true });
        track.addEventListener('touchend', function (e) {
            var d = tx - e.changedTouches[0].clientX;
            if (Math.abs(d) > 50) goTo(d > 0 ? cur + 1 : cur - 1);
        });

        window.addEventListener('resize', function () {
            buildDots();
            update();
        });

        buildDots();
        update();

        // Autoplay Loop
        var autoPlayLoop = setInterval(function() { goTo(cur + 1); }, 3500);
        track.closest('.rc3-outer').addEventListener('mouseenter', function() { clearInterval(autoPlayLoop); });
        track.closest('.rc3-outer').addEventListener('mouseleave', function() { autoPlayLoop = setInterval(function() { goTo(cur + 1); }, 3500); });
        
    })();
</script>"""

    text = text.replace(old_carousel_js, new_carousel_js)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(text)

print('Update successful.')
