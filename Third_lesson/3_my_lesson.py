# Пользователь вводит свой язоковой код, например ru, en, kg.
# А программа приветствует на его языке.
# нужно использовать if, elif, else.


# 1 способ
language = input("введите ваш язык:")
if language == "kg":
    print("Салам!")
elif language == "ru":
    print("Привет")
elif language == "en":
    print("Hello!")
else:
    print("Простите, я не знаю этот язык")


# 2 способ
language = input("введите ваш язык:")

language_greetings = {
    "kg": "Салам!",
    "ru": "Привет!",
    "en": "Hello!",
}

word = language_greetings[language]

print(word)