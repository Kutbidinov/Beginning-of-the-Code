import telebot
from file_with_token import MY_TOKEN

bot = telebot.TeleBot(MY_TOKEN)

# Определяем стадии опроса
QUESTION1, QUESTION2, QUESTION3 = range(3)

# Словарь для хранения текущего состояния пользователя
user_state = {}
user_answers = {}

def get_user_state(user_id):
    return user_state.get(user_id, None)

def set_user_state(user_id, state):
    user_state[user_id] = state

def set_user_answer(user_id, question, answer):
    if user_id not in user_answers:
        user_answers[user_id] = {}
    user_answers[user_id][question] = answer

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Привет! Давайте начнем опрос. Введите свой ответ на первый вопрос: Как вас зовут?")
    set_user_state(message.chat.id, QUESTION1)

@bot.message_handler(func=lambda message: get_user_state(message.chat.id) == QUESTION1)
def question1(message):
    set_user_answer(message.chat.id, 'name', message.text)
    bot.reply_to(message, "Спасибо! Теперь ответьте на второй вопрос: Сколько вам лет?")
    set_user_state(message.chat.id, QUESTION2)

@bot.message_handler(func=lambda message: get_user_state(message.chat.id) == QUESTION2)
def question2(message):
    set_user_answer(message.chat.id, 'age', message.text)
    bot.reply_to(message, "Отлично! Теперь ответьте на третий вопрос: Вы любите Играть Футбол?")
    set_user_state(message.chat.id, QUESTION3)

@bot.message_handler(func=lambda message: get_user_state(message.chat.id) == QUESTION3)
def question3(message):
    set_user_answer(message.chat.id, 'Game', message.text)
    answers = user_answers.get(message.chat.id, {})
    bot.reply_to(message, f"Спасибо за ответы! Вот что вы ответили:\n"
                          f"Имя: {answers.get('name')}\n"
                          f"Возраст: {answers.get('age')}\n"
                          f"Любите играть Футбол: {answers.get('Game')}")
    user_state.pop(message.chat.id, None)  # Сбрасываем состояние пользователя после завершения опроса
    user_answers.pop(message.chat.id, None)  # Удаляем ответы пользователя после завершения опроса

@bot.message_handler(commands=["Not"])
def cancel(message):
    bot.reply_to(message, "Опрос отменен. До свидания!")
    user_state.pop(message.chat.id, None)  # Сбрасываем состояние пользователя после отмены опроса
    user_answers.pop(message.chat.id, None)  # Удаляем ответы пользователя после отмены опроса

bot.infinity_polling()
