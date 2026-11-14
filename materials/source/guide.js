async function copyText(value) {
  if (navigator.clipboard && window.isSecureContext) {
    try { await navigator.clipboard.writeText(value); return true; } catch (_) {}
  }
  const field = document.createElement('textarea');
  field.value = value;
  field.setAttribute('readonly', '');
  field.style.cssText = 'position:fixed;left:-9999px;top:0';
  document.body.append(field);
  field.select();
  let copied = false;
  try { copied = document.execCommand('copy'); } catch (_) {}
  field.remove();
  return copied;
}

async function copyWithFeedback(button, value) {
  const original = button.textContent;
  const copied = await copyText(value);
  button.textContent = copied ? 'Скопировано ✓' : 'Не удалось скопировать';
  window.setTimeout(() => { button.textContent = original; }, 2400);
}

const codeBlocks = [...document.querySelectorAll('pre')];
codeBlocks.forEach((pre) => {
  const wrap = document.createElement('div');
  wrap.className = 'code-wrap';
  pre.before(wrap);
  const button = document.createElement('button');
  button.className = 'copy';
  button.type = 'button';
  button.textContent = 'Скопировать промпт целиком';
  button.addEventListener('click', () => copyWithFeedback(button, pre.textContent.trim()));
  wrap.append(button, pre);
});

const linkButtons = [];
document.querySelectorAll('main a[href^="https://"], main a[href^="http://"]').forEach((link) => {
  if (link.querySelector('img')) return;
  const button = document.createElement('button');
  button.className = 'copy-link';
  button.type = 'button';
  button.textContent = 'Скопировать ссылку';
  button.setAttribute('aria-label', `Скопировать ссылку: ${link.textContent.trim()}`);
  button.addEventListener('click', () => copyWithFeedback(button, link.href));
  link.after(button);
  linkButtons.push(link);
});

const tools = document.querySelector('.tools');
if (tools) {
  const allPrompts = document.createElement('button');
  allPrompts.className = 'copy';
  allPrompts.type = 'button';
  allPrompts.textContent = 'Скопировать все промпты';
  allPrompts.addEventListener('click', () => copyWithFeedback(allPrompts, codeBlocks.map((pre) => pre.textContent.trim()).join('\n\n──────────\n\n')));
  const allLinks = document.createElement('button');
  allLinks.className = 'copy';
  allLinks.type = 'button';
  allLinks.textContent = 'Скопировать все ссылки';
  allLinks.addEventListener('click', () => copyWithFeedback(allLinks, [...new Set(linkButtons.map((link) => link.href))].join('\n')));
  tools.append(allPrompts, allLinks);
}
