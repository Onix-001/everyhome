// Toggle du menu mobile
(function () {
    const header = document.querySelector('header.navbar');
    const toggle = document.querySelector('.nav-toggle');
    const nav    = document.querySelector('nav.primary-nav');

    if (!toggle || !header || !nav) return;

    toggle.addEventListener('click', () => {
        const isOpen = header.classList.toggle('nav-open');
        toggle.setAttribute('aria-expanded', String(isOpen));
    });

    // Fermer le menu quand on clique sur un lien (sur mobile)
    nav.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', () => {
            if (header.classList.contains('nav-open')) {
                header.classList.remove('nav-open');
                toggle.setAttribute('aria-expanded', 'false');
            }
        });
    });
})();