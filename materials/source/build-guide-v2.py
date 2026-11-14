from pathlib import Path
import markdown,fitz
from playwright.sync_api import sync_playwright
here=Path(__file__).resolve().parent
root=here.parent
body=markdown.markdown((here/'GUIDE-TWO-SITES-V2.md').read_text(),extensions=['tables','fenced_code'])
body=body.replace('<h2>4.', '<img class="shot" src="guide/nikolskaya-1440.png" alt="Пример визитки"><h2>4.').replace('<h2>5.','<img class="shot" src="guide/opora-1440.png" alt="Пример проекта"><h2>5.')
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
