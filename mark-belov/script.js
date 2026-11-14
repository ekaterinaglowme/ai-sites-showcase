const avatar = document.querySelector('.avatar');
const hero = document.querySelector('.hero');
const motion = matchMedia('(prefers-reduced-motion: reduce)');
hero.addEventListener('pointermove', event => {
  if (motion.matches || event.pointerType !== 'mouse') return;
  const r = hero.getBoundingClientRect();
  const x = (event.clientX-r.left)/r.width*2-1;
  const y = (event.clientY-r.top)/r.height*2-1;
  avatar.style.transform = `rotateY(${x*25}deg) rotateX(${-y*12}deg)`;
});
hero.addEventListener('pointerleave', () => avatar.style.transform = 'none');
motion.addEventListener('change', () => avatar.style.transform = 'none');
const dialog = document.querySelector('#contact-dialog');
document.querySelector('[data-open-contact]').addEventListener('click', () => dialog.showModal());
document.querySelector('[data-close-contact]').addEventListener('click', () => dialog.close());
document.querySelectorAll('.project-cover').forEach(link => link.addEventListener('click', () => {
 document.querySelector(link.getAttribute('href')).open = true;
}));
