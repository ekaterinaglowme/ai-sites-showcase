(() => {
  const root = document.documentElement;
  root.classList.add('is-loading');

  function reveal() {
    clearTimeout(deadline);
    const overlay = document.querySelector('.site-preloader');
    if (!overlay) {
      root.classList.remove('is-loading');
      return;
    }
    if (overlay.classList.contains('is-ready')) return;
    overlay.classList.add('is-ready');
    setTimeout(() => {
      root.classList.remove('is-loading');
      overlay.remove();
    }, 320);
  }

  const deadline = setTimeout(reveal, 6000);
  document.addEventListener('DOMContentLoaded', async () => {
    try {
      const images = [...document.querySelectorAll('[data-loader-image]')];
      await Promise.allSettled([...images.map(image => image.decode()), document.fonts.ready]);
    } finally {
      reveal();
    }
  });
})();
