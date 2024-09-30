from goto import with_goto
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
#start_markup = telebot.types.InlineKeyboardMarkup()
# Список товаров
data = {}
home_menu = {
    1: "паста",
    2: "бургер",
    3: "суши",
    4: "мой заказ"
}


pasta_menu = {
    1: {'name': 'паста 1','image': '15COOKING-PASTA-superJumbo-v2.jpg', 'price': 1},
    2: {'name': 'паста 1','image': '13346e9c4ed98dff79263307baf0cb21-1100x825.jpg', 'price': 2},
    3: {'name': 'паста 1','image': '6389174809.jpg', 'price': 3},
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
    bot.send_message(message.chat.id, '_', reply_markup=types.ReplyKeyboardRemove())


    markup = types.InlineKeyboardMarkup()

    for home_menu_id, home_menu_name in home_menu.items():
        button = types.InlineKeyboardButton(text=home_menu_name, callback_data=f'buy_{home_menu_id}')
        markup.add(button)


    bot.send_message(message.chat.id, "Вот наше меню:", reply_markup=markup)


    @bot.callback_query_handler(func=lambda call: call.data.startswith('buy_'))
    def buy_product(call):

        data = {}
        home_menu_id = int(call.data.split('_')[1])
        print(home_menu_id)
        match home_menu_id:
            case 1:

                a_price = pasta_menu[1]['price']
                image = open(pasta_menu[1]['image'], 'rb')
                print(a_price)

                start_markup.row(btn3)

                start_markup.row(inline_btn_4, inline_btn_5)

                bot.send_photo(call.message.chat.id, image, caption={a_price}, reply_markup=start_markup)


                @bot.callback_query_handler(func=lambda popa: popa.data.startswith('buk_'))
                def chenge_product(popa):
                    kuda= int(popa.data.split('_')[1])
                    match kuda:
                        case 1:
                            a_price = pasta_menu[1]['price']
                            a_name = pasta_menu[1]['name']
                            data = a_price,a_name
                            print(data)
                        case 4:
                            print()

                            a_price = pasta_menu[2]['price']
                            image = open(pasta_menu[2]['image'], 'rb')
                            print(a_price)

                            start_markup.row(btn3)

                            start_markup.row(inline_btn_3, inline_btn_4, inline_btn_5)

                            bot.send_photo(call.message.chat.id, image, caption={a_price}, reply_markup=start_markup)

                            @bot.callback_query_handler(func=lambda popa: popa.data.startswith('buk_'))
                            def chenge_product(popa):
                                kuda = int(popa.data.split('_')[1])
                                match kuda:
                                    case 1:
                                        a_price = pasta_menu[1]['price']
                                        a_name = pasta_menu[1]['name']
                                        data = a_price, a_name
                                        print(data)

                        case 3:
                            show_products(message)
            case 2:
                pass

            case 3:
                print("перни")

"""
product_id = int(call.data.split('_')[1])

    product_name = home_menu[product_id]
    match product_name:
        case "Товар 1 - 100 ₽":
            bot.send_message(admin_id, f"Пользователь @{call.from_user.username} купил: писю бобра")
        case "Товар 2 - 200 ₽":
            print('1')
        case "Товар 3 - 300 ₽":
            print("перни")
    bot.send_message(admin_id, f"Пользователь @{call.from_user.username} купил: {product_name}")
    bot.send_message(call.message.chat.id, f"Вы купили: {product_name}. Спасибо за покупку!")
"""
# Запуск бота
bot.polling(none_stop=True)
