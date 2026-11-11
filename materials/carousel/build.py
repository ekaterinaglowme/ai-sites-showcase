from PIL import Image, ImageDraw, ImageFont, ImageOps
from pathlib import Path
P=Path(__file__).resolve().parent; S=P.parent/'guide'
F='/System/Library/Fonts/Supplemental/'
def font(n,b=False):return ImageFont.truetype(F+('Arial Bold.ttf' if b else 'Arial.ttf'),n)
bg='#0b0c0e';white='#f6f5f0';blue='#91afff';muted='#aeb3bd'
def text(s,x,y,size=35,color=white,b=False,width=940):
 global d
 yy=y
 for para in s.split('\n'):
  line=''
  for w in para.split():
   q=(line+' '+w).strip()
   if d.textlength(q,font=font(size,b))>width and line:
    d.text((x,yy),line,font=font(size,b),fill=color);yy+=size*1.23;line=w
   else:line=q
  d.text((x,yy),line,font=font(size,b),fill=color);yy+=size*1.23
 return yy

def shot(name,box):
 im=Image.open(S/name).convert('RGB'); im=ImageOps.contain(im,(box[2],box[3])); canvas.paste(im,(box[0]+(box[2]-im.width)//2,box[1]))
def base(i,k,title):
 global canvas,d
 canvas=Image.new('RGB',(1080,1350),bg);d=ImageDraw.Draw(canvas)
 text('@NIKOLSKAYA.AI',65,45,23,blue,True);text(f'{i:02} / 09',900,45,23,blue)
 d.line((65,96,1015,96),fill='#363a43',width=2)
 text(k.upper(),65,135,23,blue,True);text(title,65,190,76,white,True)
 d.line((65,1240,1015,1240),fill='#363a43',width=2);text('СВОЙ САЙТ С ИИ',65,1270,22,muted);text('ЛИСТАЙ →' if i<9 else 'СОХРАНИ 💙'.replace(' 💙',''),830,1270,22,blue)
def save(i):canvas.save(P/f'{i:02}.jpg',quality=94,subsampling=0)
base(1,'Практика / без кода','СВОЙ САЙТ.\nС ПОМОЩЬЮ ИИ.')
text('От идеи до первого результата —\nна моих реальных примерах.',65,405,35,muted)
shot('nikolskaya-1440.png',(65,535,950,660));save(1)
base(2,'01 / Задача','Сначала —\nчто за сайт?')
text('Визитка, школа, студия или компания?\nРасскажи ИИ, кому и зачем он нужен.',65,405,36,muted)
text('«Создай сайт для [кого].\nМоя аудитория — [кто].\nГлавное действие — [написать /\nзаписаться / посмотреть проекты].\nВот мои тексты и фотографии…»',85,615,39,white)
text('Подставляй свою информацию.\nНе проси ИИ выдумывать опыт и отзывы.',65,1050,32,blue);save(2)
base(3,'02 / Референс','Покажи стиль.\nНе угадывай слова.')
text('Найди сайт, который нравится.\nПрикрепи скриншот и уточни детали:',65,410,35,muted)
shot('opora-1440.png',(65,535,950,440))
text('«Нравятся крупные буквы, тёплый фон\nи свободная композиция. Адаптируй\nэтот подход под мои тексты».',65,1020,34,white);save(3)
base(4,'03 / Первый результат','Не нравится?\nСкринь и объясняй.')
text('Один скриншот + одна конкретная правка.\nТак проще получить нужный результат.',65,415,35,muted)
text('ВМЕСТО «СДЕЛАЙ КРАСИВО»',65,620,25,blue,True)
text('«Увеличь пробелы между словами».\n\n«Выровняй логотип по левому краю\nзаголовка».\n\n«Оставь три фотографии.\nОни не должны перекрывать текст».',65,685,37)
save(4)
base(5,'04 / Цвет','Нужен цвет?\nПокажи его.')
text('Сохрани палитру или скрин из Pinterest\nи приложи к своему запросу.',65,415,35,muted)
for j,c in enumerate(['#f3eee3','#101010','#91afff']):
 d.rounded_rectangle((65+j*325,570,365+j*325,830),radius=15,fill=c)
text('«Возьми цвета с этого изображения:\nсветлый — для фона, тёмный — для текста,\nголубой — для кнопок и акцентов».',65,915,36)
save(5)
base(6,'05 / Свои фотографии','Меняй картинки.\nМеняй ощущение.')
text('Стоковые фото замени на те,\nкоторые подходят именно твоему проекту.',65,415,35,muted)
shot('case-2-after.png',(65,540,950,460))
text('«Первое фото поставь в левую карточку,\nвторое — в правую. Сохрани пропорции,\nне растягивай и не меняй цвет».',65,1040,33);save(6)
base(7,'06 / Личный визуал','А можно —\nсвою 3D-голову.')
text('Прикрепи своё фото и попроси создать\nстилизованный портрет для первого экрана.',65,410,34,muted)
head=P.parents[1]/'nikolskaya-romans/assets/katya-head.png'
if not head.exists():head=next((P.parents[1]/'nikolskaya-romans').rglob('katya-head.png'))
im=Image.open(head).convert('RGBA');im.thumbnail((490,570));canvas.paste(im,(560,570),im)
text('«Сохрани мои черты.\nГлянцевый 3D-стиль,\nмягкий студийный свет.\nТолько голова,\nпрозрачный фон».',65,650,34,width=480)
text('PNG — картинка. Для настоящего вращения\nсо всех сторон нужна отдельная 3D-модель.',65,1135,27,blue);save(7)
base(8,'07 / Проверка','Проверь.\nСохрани.\nПотом публикуй.')
text('01   Открой сайт на телефоне.\n\n02   Проверь текст, фото и кнопки.\n\n03   Сохрани удачную версию.\n\n04   Запиши, что ещё нужно поправить.',65,580,38)
text('Во втором уроке — GitHub и деплой:\nкак выложить сайт и получить ссылку.',65,1080,34,blue);save(8)
base(9,'Полный гайд / 30 страниц','ХОЧЕШЬ\nПОВТОРИТЬ?')
text('Собрала пошаговый гайд:\nот пустой папки до своего сайта.',65,430,39,muted)
text('Промпты с местом для твоих текстов.\nСкиллы и инструкции по установке.\nМои примеры доработки дизайна.',65,620,35)
d.rounded_rectangle((65,880,1015,1100),radius=20,fill=blue)
text('НАПИШИ «САЙТ»',100,925,58,'#0b0c0e',True)
text('в комментариях — пришлю гайд',100,1010,35,'#0b0c0e')
save(9)
thumb=Image.new('RGB',(810,1014),'#222222')
for i in range(1,10):
 im=Image.open(P/f'{i:02}.jpg');im.thumbnail((270,338));thumb.paste(im,(((i-1)%3)*270,((i-1)//3)*338))
thumb.save(P/'preview.jpg',quality=90)
