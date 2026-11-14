from pathlib import Path
import markdown,fitz,re
from playwright.sync_api import sync_playwright
here=Path(__file__).resolve().parent
root=here.parent
body=markdown.markdown((here/'GUIDE-TWO-SITES-V2.md').read_text(),extensions=['tables','fenced_code'])
for heading, image, caption in [
 ('4. Сайт-визитка — два промпта по порядку', 'nikolskaya-1440.png', 'Сайт-визитка — Екатерина Никольская. Референс: готовый сайт Екатерины.'),
 ('5. Сайт проекта — один цельный промпт', 'opora-1440.png', 'Сайт проекта — школа «Опора». Референс: готовый сайт «Опора».'),
]:
 title = '<h2>' + heading + '</h2>'
 assert title in body
 body = body.replace(title, title + '<figure class="site-example"><img class="shot" src="guide/' + image + '" alt="' + caption + '"><figcaption>' + caption + '</figcaption></figure>')
page='<!doctype html><html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Сайт с ИИ — гайд и промпты</title><style>'+(here/'guide.css').read_text()+'</style></head><body><main><div class="brand">@NIKOLSKAYA.AI · УРОК 01</div><div class="tools"><a href="guide/Гайд-и-все-промпты.txt">Скачать весь текст</a><a href="guide/Ваш-сайт-с-ИИ-полный-гайд.pdf">PDF для сохранения</a></div>'+body+'</main><script>'+(here/'guide.js').read_text()+'</script></body></html>'
(root/'index.html').write_text(page)
(root/'guide/guide.html').write_text(page.replace('href="guide/','href="').replace('src="guide/','src="'))
for name in ['Гайд-и-все-промпты.txt','Промпты-и-инструкции.md']:(root/'guide'/name).write_text((here/'GUIDE-TWO-SITES-V2.md').read_text())
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless=True)
 page=b.new_page();page.goto((root/'index.html').as_uri(),wait_until='load')
 target=root/'guide/Ваш-сайт-с-ИИ-полный-гайд.pdf'
 page.pdf(path=str(target),print_background=True,prefer_css_page_size=True);b.close()
d=fitz.open(target)
for p in d:p.draw_rect(p.rect,color=None,fill=(16/255,18/255,18/255),overlay=False)
d.save(str(target)+'.tmp');d.close();Path(str(target)+'.tmp').replace(target)

# Synchronize every downloadable prompt from the canonical guide.
source=(here/'GUIDE-TWO-SITES-V2.md').read_text()
(here/'GUIDE-TWO-SITES-FROM-ZERO.md').write_text(source)
personal_section=source.split('## 4.',1)[1].split('## 5.',1)[0]
project_section=source.split('## 5.',1)[1].split('## 6.',1)[0]
personal_prompts=re.findall(r'```text\n(.*?)\n```',personal_section,re.S)
project_prompts=re.findall(r'```text\n(.*?)\n```',project_section,re.S)
assert len(personal_prompts)==2 and len(project_prompts)==1
for prompt,filename,markdown_file,note in [
 (personal_prompts[0], 'Промпт-3D-аватар.txt', 'PROMPT-3D-AVATAR.md', 'Приложите своё чёткое фото лица и полную картинку-образец с аватаром и текстом из гайда, затем доработайте результат в чате до сохранения.'),
 (personal_prompts[1], 'Промпт-сайт-визитка.txt', 'PROMPT-PERSONAL-WEBSITE.md', 'Приложите готовый 3D-аватар и отдельную обычную фотографию для блока «Обо мне».'),
 (project_prompts[0], 'Промпт-сайт-проекта.txt', 'PROMPT-COMPANY-WEBSITE.md', 'Установите скиллы по гайду, заполните поля и приложите фотографии проекта.'),
]:
 (root/'guide'/filename).write_text(prompt+'\n')
 (here/markdown_file).write_text('# '+filename.removesuffix('.txt').replace('-', ' ')+'\n\n'+note+'\n\n```text\n'+prompt+'\n```\n')
