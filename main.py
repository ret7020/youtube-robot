import requests, time
from PIL import Image, ImageDraw, ImageFont
import ctypes, os
channel_id = "ID НУЖНОГО КАНЛА"
api_key = "API КЛЮЧ"
while True:
    data = requests.get("https://www.googleapis.com/youtube/v3/channels?id=" + channel_id + "&part=statistics&key=" + api_key).json()
    print(data)
    print(data['items'][0]['statistics']['viewCount'])
    im =  Image.open(r"images/background.jpg")
    font = ImageFont.truetype(r'fonts/8693.ttf', size=68) #Мой шрифт в папке font
    draw_text = ImageDraw.Draw(im)
    draw_text.text(
        (100, 100),
        'Подписчиков: ' + data['items'][0]['statistics']['subscriberCount'] + "\nПросмотров: " + data['items'][0]['statistics']['viewCount'] + "\nВсего видосов: " + data['items'][0]['statistics']['videoCount'],
        font=font,
        fill='red')
    im.save(r"result.png", "PNG")
    ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.join(os.getcwd(), "result.png"), 0)
    time.sleep(15)
#Для установки необходимых библиотек: pip install Pillow requests
