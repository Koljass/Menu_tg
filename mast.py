from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters, CallbackContext

# Токен, который вы получили от BotFather
TOKEN = 'your-telegram-bot-token'

# Меню шаурмы
menu = {
    "Шаурма куриная": 250,
    "Шаурма говяжья": 300,
    "Шаурма с картошкой": 350,
    "Шаурма в лаваше": 200,
}

# Стартовая команда
def start(update: Update, context: CallbackContext):
    user = update.message.from_user
    update.message.reply_text(f"Привет, {user.first_name}! Я бот для доставки шаурмы. Выберите блюдо из меню ниже.", reply_markup=main_menu())

# Главное меню с кнопками
def main_menu():
    keyboard = [
        [InlineKeyboardButton(name, callback_data=name)] for name in menu.keys()
    ]
    keyboard.append([InlineKeyboardButton("Заказать", callback_data='order')])
    return InlineKeyboardMarkup(keyboard)

# Обработка выбора блюда
def button(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    dish = query.data

    if dish == 'order':
        order_text = "Выберите блюда для заказа:\n"
        for item, price in menu.items():
            order_text += f"{item} - {price}₽\n"
        query.edit_message_text(order_text)
    else:
        price = menu.get(dish)
        if price:
            query.edit_message_text(f"Вы выбрали {dish}. Стоимость: {price}₽\nХотите добавить это в заказ?", reply_markup=order_confirmation(dish, price))

# Подтверждение добавления блюда в заказ
def order_confirmation(dish, price):
    keyboard = [
        [InlineKeyboardButton("Да", callback_data=f'confirm_{dish}_{price}')],
        [InlineKeyboardButton("Нет", callback_data="order")]
    ]
    return InlineKeyboardMarkup(keyboard)

# Подтверждение или отмена заказа
def confirm_order(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    data = query.data.split('_')
    
    if data[0] == 'confirm':
        dish, price = data[1], data[2]
        query.edit_message_text(f"Вы добавили {dish} за {price}₽ в ваш заказ.")
    else:
        query.edit_message_text("Возвращаемся в главное меню.", reply_markup=main_menu())

# Обработка текстовых сообщений (если клиент хочет задать вопрос)
def handle_text(update: Update, context: CallbackContext):
    user_message = update.message.text.lower()
    if 'привет' in user_message or 'здравствуйте' in user_message:
        update.message.reply_text("Здравствуйте! Я бот доставки шаурмы. Как могу помочь?")
    else:
        update.message.reply_text("Извините, я вас не понял. Выберите опцию из меню.")

def main():
    # Создание updater и dispatcher
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Обработчики
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CallbackQueryHandler(button))
    dispatcher.add_handler(CallbackQueryHandler(confirm_order, pattern=r'confirm_'))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_text))

    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
