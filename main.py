import qrcode
img = qrcode.make('GitHub Webhook')
img.save("gitHub_webhook.png")
#this string create before installation ngrok
#эта строка для 3-й попытки подключить github к jenkins
#гитхаб снова ругается, пробую это исправить....
#ммммммммммммм моя любимая 403 ошибка, вот в чем дело было, класс. Включил впн.
