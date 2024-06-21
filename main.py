import telebot
from telebot import types

BOT_TOKEN = '7038256245:AAGVh50jRTsmhwNg-TcjW-2tvpPOI-jUQtw'  

bot = telebot.TeleBot(BOT_TOKEN)


def create_buttons(items):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for item in items:
        markup.add(types.KeyboardButton(item))
    return markup


def choose_lash_volume():
    return create_buttons([
        '2D',
        '3D',
        '4D',
        'Mega Volume' 
    ])


def choose_lash_effect():
    return create_buttons([
        'Естественный',
        'Кукольный',
        'Лисий',
        'Беличий'
    ])


def choose_lash_color():
    return create_buttons([
        'Черные',
        'Шоколад',
        'Цветные'
    ])


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! Я помогу тебе подобрать объем, эффект, цвет для наращивания ресниц.🥰\n\nКакой цвет ресниц тебе интересен?', reply_markup=choose_lash_color())


@bot.message_handler(func=lambda message: message.text in ['Черные', 'Шоколад', 'Цветные'])
def handle_lash_color(message):
    if message.text in ['Черные', 'Шоколад', 'Цветные']:
        bot.send_message(message.chat.id, f'Замечательно, {message.text}! 👌\n\nКакой объем ресниц тебе интересен?', reply_markup=choose_lash_volume())
    
        if message.text == 'Черные':
            bot.send_photo(message.chat.id, open('photo1718970246.jpeg', 'rb'))  
        elif message.text == 'Шоколад':
            bot.send_photo(message.chat.id, open('photo1718970239.jpeg', 'rb')) 
        elif message.text == 'Цветные':
            bot.send_photo(message.chat.id, open('photo1718970263.jpeg', 'rb')) 


@bot.message_handler(func=lambda message: message.text in ['2D', '3D', '4D', 'Mega Volume'])
def handle_lash_volume(message):
    if message.text in ['2D', '3D', '4D', 'Mega Volume']:
        bot.send_message(message.chat.id, f'Отлично, {message.text}! 👌\n\nКакой эффект ресниц ты хочешь?', reply_markup=choose_lash_effect())
        
        if message.text == '2D':
            bot.send_photo(message.chat.id, open('photo1718969673.jpeg', 'rb')) 
        elif message.text == '3D':
            bot.send_photo(message.chat.id, open('photo1718969673 (1).jpeg', 'rb')) 
        elif message.text == '4D':
            bot.send_photo(message.chat.id, open('photo1718969673 (3).jpeg', 'rb')) 
        elif message.text == 'Mega Volume':
            bot.send_photo(message.chat.id, open('photo1718969673 (4).jpeg', 'rb')) 


@bot.message_handler(func=lambda message: message.text in ['Естественный', 'Кукольный', 'Лисий', 'Беличий'])
def handle_lash_effect(message):
    if message.text in ['Естественный', 'Кукольный', 'Лисий', 'Беличий']:
        bot.send_message(message.chat.id, f'Супер, {message.text}! 👌\n\nЯ подберу для тебя идеальный вариант!')
        
        if message.text == 'Естественный':
            bot.send_photo(message.chat.id, open('msg928312113-373406.jpg', 'rb')) 
        elif message.text == 'Кукольный':
            bot.send_photo(message.chat.id, open('photo1718969051.jpeg', 'rb')) 
        elif message.text == 'Лисий':
            bot.send_photo(message.chat.id, open('photo1718969049.jpeg', 'rb')) 
        elif message.text == 'Беличий':
            bot.send_photo(message.chat.id, open('photo1718969054.jpeg', 'rb')) 

bot.polling()
