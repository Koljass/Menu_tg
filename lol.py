import telebot
from telebot import types

# Замените на свой токен, который вы получили от BotFather
TOKEN = '8016150551:AAFFYyAbq4DJZv58rxdKle4M7Wsl94VE04c'
bot = telebot.TeleBot(TOKEN)

# Меню шаурмы
menu = {
    'Классическая шаурма': 200,
    'Шаурма с курицей': 250,
    'Шаурма с говядиной': 300,
    'Шаурма с овощами': 150
}

# Команда /start
@bot.message_handler(commands=['start'])
def start(message):
    # Приветственное сообщение
    bot.send_message(message.chat.id, "Привет! Я бот для заказа шаурмы. Введите /menu, чтобы увидеть меню.")

# Команда /menu - Показывает меню
@bot.message_handler(commands=['menu'])
def show_menu(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    for item in menu:
        markup.add(types.KeyboardButton(item))
    
    bot.send_message(message.chat.id, "Выберите шаурму из меню:", reply_markup=markup)

# Обработка выбора из меню
@bot.message_handler(func=lambda message: message.text in menu)
def process_order(message):
    choice = message.text
    price = menu[choice]
    
    # Оповещаем пользователя о выбранной шаурме и цене
    bot.send_message(message.chat.id, f"Вы выбрали {choice}. Цена: {price} руб.\nДля оформления заказа нажмите /order.")
    
    # Ожидаем команду для оформления заказа
    @bot.message_handler(commands=['order'])
    def confirm_order(msg):
        if msg.chat.id == message.chat.id:
            bot.send_message(msg.chat.id, f"Ваш заказ: {choice} на сумму {price} руб.\nСпасибо за заказ!")
            bot.send_message(msg.chat.id, "Ваш заказ будет доставлен в ближайшее время!")
            # Здесь можно добавить дальнейшую логику для оформления заказа (например, адрес доставки)
            # После завершения заказа, можно сбросить меню
            bot.send_message(msg.chat.id, "Чтобы заказать снова, введите /menu.")

# Обработчик текстовых сообщений (если введена команда, которой нет в списке)
@bot.message_handler(func=lambda message: True)
def handle_text(message):
    bot.send_message(message.chat.id, "Извините, я вас не понял. Напишите /menu, чтобы выбрать шаурму.")

# Запуск бота
bot.polling(none_stop=True)