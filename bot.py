import telebot
import re
from telebot import types
import requests
from bs4 import BeautifulSoup



bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcom(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Игроков на севере')
    item2 = types.KeyboardButton('Карта')
    item3 = types.KeyboardButton('Чекать до 0')
    item4 = types.KeyboardButton('Чекать до 5')
    item5 = types.KeyboardButton('Чекать до 10')
    item6 = types.KeyboardButton('Чекать до 15')
    item7 = types.KeyboardButton('Чекать до 20')
    item8 = types.KeyboardButton('Чекать до 25')
    item9 = types.KeyboardButton('Чекать до 30')
    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9)
    sti = open('sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, 'Добро пожаловать, <strong>{0.first_name}</strong>!\nЯ <strong>{1.first_name}</strong>!\nМой создатель <strong>Anonymous</strong>.\nЭтот бот был создан с целью узнать, что и как на\n<strong>"SFW - UKRAINE"</strong> прямо с <strong>ТЕЛЕФОНА</strong>.\nВаш <strong>{1.first_name}</strong>...'.format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)

@bot.message_handler(commands=['stop'])
@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Игроков на севере':
            URLKA_1 = 'http://cs.sfw.so/?r=serverinfo/view&id=1'
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
            full_page1 = requests.get(URLKA_1, headers=headers)
            soup1 = BeautifulSoup(full_page1.content, 'html.parser')
            convert1 = soup1.findAll("tr")
            peoples = convert1[-2].text
            peoples = str(peoples)
            peoples = re.sub(r"[Игроки:]", "", peoples)
            peoples = peoples.strip()
            bot.send_message(message.chat.id, str(f'Сейчас на сервере игроков >>> {peoples}.'))
        elif message.text == 'Карта':
            URLKA_1 = 'http://cs.sfw.so/?r=serverinfo/view&id=1'
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
            full_page1 = requests.get(URLKA_1, headers=headers)
            soup1 = BeautifulSoup(full_page1.content, 'html.parser')
            convert1 = soup1.findAll("tr")
            map_text = convert1[-3].text
            map_text = str(map_text)
            map_text = re.sub(r'[Карт:]', '', map_text)
            map_text = map_text.strip()
            bot.send_message(message.chat.id, str(f'На данный момент карта такая >>> {map_text}'))
        elif message.text == 'Чекать до 0':
            bot.send_message(message.chat.id, str('\"Чекать...\" - это моя функция, позволяющяя вам получить уведомление, когда на сервере будет нужное кол-во (X) игроков.'))
            bot.send_message(message.chat.id, str('Чекаю...'))
            while True:
                URLKA_1 = 'http://cs.sfw.so/?r=serverinfo/view&id=1'
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
                full_page1 = requests.get(URLKA_1, headers=headers)
                soup1 = BeautifulSoup(full_page1.content, 'html.parser')
                convert1 = soup1.findAll("tr")
                peoples = convert1[-2].text
                peoples = str(peoples)
                peoples = re.sub(r"[Игроки:]", "", peoples)
                peoples = peoples.strip()
                peoples = peoples[:-3]
                peoples = int(peoples)
                if peoples == 0:
                    bot.send_message(message.chat.id, str('На сервере 0 игроков'))
                    break
                elif peoples != 0:
                    continue
        elif message.text == 'Чекать до 5':
            bot.send_message(message.chat.id, str('\"Чекать...\" - это моя функция, позволяющяя вам получить уведомление, когда на сервере будет нужное кол-во (X) игроков.'))
            bot.send_message(message.chat.id, str('Чекаю...'))
            while True:
                URLKA_1 = 'http://cs.sfw.so/?r=serverinfo/view&id=1'
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
                full_page1 = requests.get(URLKA_1, headers=headers)
                soup1 = BeautifulSoup(full_page1.content, 'html.parser')
                convert1 = soup1.findAll("tr")
                peoples = convert1[-2].text
                peoples = str(peoples)
                peoples = re.sub(r"[Игроки:]", "", peoples)
                peoples = peoples.strip()
                peoples = peoples[:-3]
                peoples = int(peoples)
                if peoples == 5:
                    bot.send_message(message.chat.id, str('На сервере 5 игроков'))
                    break
                elif peoples != 5:
                    continue
        elif message.text == 'Чекать до 10':
            bot.send_message(message.chat.id, str('\"Чекать...\" - это моя функция, позволяющяя вам получить уведомление, когда на сервере будет нужное кол-во (X) игроков.'))
            bot.send_message(message.chat.id, str('Чекаю...'))
            while True:
                URLKA_1 = 'http://cs.sfw.so/?r=serverinfo/view&id=1'
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
                full_page1 = requests.get(URLKA_1, headers=headers)
                soup1 = BeautifulSoup(full_page1.content, 'html.parser')
                convert1 = soup1.findAll("tr")
                peoples = convert1[-2].text
                peoples = str(peoples)
                peoples = re.sub(r"[Игроки:]", "", peoples)
                peoples = peoples.strip()
                peoples = peoples[:-3]
                peoples = int(peoples)
                if peoples == 10:
                    bot.send_message(message.chat.id, str('На сервере 10 игроков'))
                    break
                elif peoples != 10:
                    continue
        elif message.text == 'Чекать до 15':
            bot.send_message(message.chat.id, str('\"Чекать...\" - это моя функция, позволяющяя вам получить уведомление, когда на сервере будет нужное кол-во (X) игроков.'))
            bot.send_message(message.chat.id, str('Чекаю...'))
            while True:
                URLKA_1 = 'http://cs.sfw.so/?r=serverinfo/view&id=1'
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
                full_page1 = requests.get(URLKA_1, headers=headers)
                soup1 = BeautifulSoup(full_page1.content, 'html.parser')
                convert1 = soup1.findAll("tr")
                peoples = convert1[-2].text
                peoples = str(peoples)
                peoples = re.sub(r"[Игроки:]", "", peoples)
                peoples = peoples.strip()
                peoples = peoples[:-3]
                peoples = int(peoples)
                if peoples == 15:
                    bot.send_message(message.chat.id, str('На сервере 15 игроков'))
                    break
                elif peoples != 15:
                    continue
        elif message.text == 'Чекать до 20':
            bot.send_message(message.chat.id, str('\"Чекать...\" - это моя функция, позволяющяя вам получить уведомление, когда на сервере будет нужное кол-во (X) игроков.'))
            bot.send_message(message.chat.id, str('Чекаю...'))
            while True:
                URLKA_1 = 'http://cs.sfw.so/?r=serverinfo/view&id=1'
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
                full_page1 = requests.get(URLKA_1, headers=headers)
                soup1 = BeautifulSoup(full_page1.content, 'html.parser')
                convert1 = soup1.findAll("tr")
                peoples = convert1[-2].text
                peoples = str(peoples)
                peoples = re.sub(r"[Игроки:]", "", peoples)
                peoples = peoples.strip()
                peoples = peoples[:-3]
                peoples = int(peoples)
                if peoples == 20:
                    bot.send_message(message.chat.id, str('На сервере 20 игроков'))
                    break
                elif peoples != 20:
                    continue
        elif message.text == 'Чекать до 25':
            bot.send_message(message.chat.id, str('\"Чекать...\" - это моя функция, позволяющяя вам получить уведомление, когда на сервере будет нужное кол-во (X) игроков.'))
            bot.send_message(message.chat.id, str('Чекаю...'))
            while True:
                URLKA_1 = 'http://cs.sfw.so/?r=serverinfo/view&id=1'
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
                full_page1 = requests.get(URLKA_1, headers=headers)
                soup1 = BeautifulSoup(full_page1.content, 'html.parser')
                convert1 = soup1.findAll("tr")
                peoples = convert1[-2].text
                peoples = str(peoples)
                peoples = re.sub(r"[Игроки:]", "", peoples)
                peoples = peoples.strip()
                peoples = peoples[:-3]
                peoples = int(peoples)
                if peoples == 25:
                    bot.send_message(message.chat.id, str('На сервере 25 игроков'))
                    break
                elif peoples != 25:
                    continue
        elif message.text == 'Чекать до 30':
            bot.send_message(message.chat.id, str('\"Чекать...\" - это моя функция, позволяющяя вам получить уведомление, когда на сервере будет нужное кол-во (X) игроков.'))
            bot.send_message(message.chat.id, str('Чекаю...'))
            while True:
                URLKA_1 = 'http://cs.sfw.so/?r=serverinfo/view&id=1'
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
                full_page1 = requests.get(URLKA_1, headers=headers)
                soup1 = BeautifulSoup(full_page1.content, 'html.parser')
                convert1 = soup1.findAll("tr")
                peoples = convert1[-2].text
                peoples = str(peoples)
                peoples = re.sub(r"[Игроки:]", "", peoples)
                peoples = peoples.strip()
                peoples = peoples[:-3]
                peoples = int(peoples)
                if peoples == 30:
                    bot.send_message(message.chat.id, str('На сервере 30 игроков'))
                    break
                elif peoples != 30:
                    continue

        else:
            bot.send_message(message.chat.id, str('ЗАПРОС НЕ НАЙДЕН'))

# RUN
bot.polling(none_stop=True)
