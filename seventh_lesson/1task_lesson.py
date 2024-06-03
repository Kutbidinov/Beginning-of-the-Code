
import random
import telebot

TOKEN = "ВАШ ТОКЕН"
bot = telebot.TeleBot(TOKEN)


random_number = random.randint(1, 101)


@bot.message_handler(commands=["start"])  # это декоратор нужен чтобы данная функция сработало когда пользователь напишет команду start
def send_welcome(message):
    bot.reply_to(message, "Привет! Я ваш бот! Вы запустили команду /start.")


@bot.message_handler(func=lambda message: True)  # этот декоратор для того чтобы отвечать на ОБЫЧНЫЕ текстовые сообщения
def answer_for_simple_text(message):
    message
    try:
        text = int(message.text)  # тип str
    except ValueError:
        bot.reply_to(message, "вы ввели не число!")
        return None

    if text > random_number:
        bot.reply_to(message, "Загаданное число меньше")
    elif text < random_number:
        bot.reply_to(message, "Загаданное число больше указанного")
    elif text == random_number:
        bot.reply_to(message, "ВЫ УГАДАЛИ ЧИСЛО")

    # if text == "привет":
    #     bot.reply_to(message, "И тебе привет!")
    # elif text == "пока":
    #     bot.reply_to(message, "И тебе пока!")
    # else:
    #     bot.reply_to(message, "Извините я пока не умею отвечать такое")


bot.infinity_polling()
