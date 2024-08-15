# напечатать от 0 до 9

# 1 способ
# for i in range(10):
#     print(i)


# напечатайте с помощью цикла while все четные число от 0 до 10


# circle = 0
# while True:  # бесконечный цикл
#     circle += 1
#     print(circle)
#     if circle == 10:
#         break

# пользователь сам заполняет лист
# вы можете перестать добавлять номера если введете 0
my_list = []
# my_list.append(10)  # метод добавляет элемент в лист
# while True:
#     number = int(input('введите ваше число'))
#     if number == 0:
#         break
#     my_list.append(number)
#
# print(my_list)

# Задача: пользователь сам заполняет лист.
# если положительные числа добавляем если отрицательные просто игнорируем
# # вы можете перестать добавлять номера если введете 0


password_pincode = "1234"
while True:
    user_password = input("введите пароль:")
    if password_pincode == user_password:
        print("ПАРОЛЬ ПРАВИЛЬНЫЙ")
        break
    else:
        print("НЕКОРРЕКТНЫЙ ПАРОЛЬ, ВВЕДИТЕ ЕЩЕ РАЗ:")

print('ВЫ ВОШЛИ')