import telebot
from telebot import types

bot = telebot.TeleBot("5858523280:AAHFa0NAmWp8KPd6qCXKVg_nyBh7fobD6Xk")

@bot.message_handler(commands=["start"])
def math(message):
    mess=f"Привет, <u>{message.from_user.first_name} {message.from_user.username}</u>"
    bot.send_message(message.chat.id, mess, parse_mode="html")


@bot.message_handler(commands=["help"])
def get_website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button1 = types.KeyboardButton("Website1")
    button2 = types.KeyboardButton("Website2")
    markup.add(button1,button2)
    bot.send_message(message.chat.id,"Выберите вебсайт", reply_markup=markup)

@bot.message_handler(content_types=["text"])
def text(message):
    if message.text == "Hello":
        bot.send_message(message.chat.id, text="<b>И тебе привет</b>", parse_mode='html')
    if message.text == "How are u?":
        bot.send_message(message.chat.id, text="<b>Fine, what about u?</b>", parse_mode="html")
    if message.text == "Fine" or message.text == "fine":
        bot.send_message(message.chat.id, text="<u>nice</u>", parse_mode="html" )

    if message.text == "Photo" or message.text == "photo":
        text = "Great Britain and Russia are the best"
        photo = open("Rect.jpg", "rb")
        bot.send_photo(message.chat.id,photo,text)
    elif message.text == "website":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Website", url="https://www.youtube.com/")
        button2 = types.InlineKeyboardButton("Website2", url="https://qiwi.com/")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, "Выберите вебсайт", reply_markup=markup)


@bot.message_handler(content_types=["photo"])
def get_photo(message):
    bot.send_message(message.chat.id, "beautiful photo bro", parse_mode="html")



bot.polling(none_stop=True)