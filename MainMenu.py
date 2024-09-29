import telebot
from telebot import types
admin_id = '1202757532'
product_name ={}
product_data ={}
start_markup = telebot.types.InlineKeyboardMarkup(row_width=3)
inline_btn_3 = types.InlineKeyboardButton('назад', callback_data=f'buk_{2}')
inline_btn_4 = types.InlineKeyboardButton('главное меню', callback_data=f'buk_{3}')
inline_btn_5 = types.InlineKeyboardButton('вперед', callback_data=f'buk_{4}')
btn3 = telebot.types.InlineKeyboardButton('выбрать', callback_data=f'buk_{1}')
API_TOKEN = '7001627716:AAFtqdhmzsiymdpZnq4yOrkOkFDDb82VrFM'
bot = telebot.TeleBot(API_TOKEN)
home_menu = {
    1: "Популярные блюда",
    2: "Салаты",
    3: "Закуски",
    4: "Супы",
    5: "Пицца",
    6: "Шашлык",
    7: "Горячие блюда",
    8: "Гарниры",
    9: "Детское меню",
    10: "Выпечка",
    11: "Десерты",
    12: "Напитки",
    13: "Соусы"
}
salati = {
    1: "Салат Азия",
    2: "Салат Ташкентский",
    3: "Салат Лаззат",
    4: "Салат Ачик-чучук",
    5: "",
    6: "",
    7: "",
    8: "",
    9: "",
    10: "",
    11: "",
}
@bot.message_handler(commands=['start'])
def start(message):
    global data
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton("Посмотреть меню")
    markup.add(button)
    bot.send_message(message.chat.id, "Добро пожаловать в кафе! Нажмите на кнопку ниже для просмотра меню.", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Посмотреть меню")
def show_products(message):
    markup = types.InlineKeyboardMarkup()

    for home_menu_id, home_menu_name in home_menu.items():
        button = types.InlineKeyboardButton(text=home_menu_name, callback_data=f'buy_{home_menu_id}')
        markup.add(button)


    bot.send_message(message.chat.id, "Вот наше меню:", reply_markup=markup)


    @bot.callback_query_handler(func=lambda call: call.data.startswith('buy_'))
    def show_products(call):
        markup = types.InlineKeyboardMarkup()
1
        for home_menu_id, home_menu_name in home_menu.items():
            button = types.InlineKeyboardButton(text=home_menu_name, callback_data=f'buy_{home_menu_id}')
            markup.add(button)

        bot.send_message(message.chat.id, "Вот наше меню:", reply_markup=markup)


