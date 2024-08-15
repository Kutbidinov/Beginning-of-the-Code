number = 123  # integer
number2 = 123.8  # float
fruit = "яблоко"  # string
is_right = True  # boolean

# структуры данных
my_list = [12, 15, 1235, 28, 17.5]  # list (*на русском список)
print(my_list[0])  # 12
print(my_list[1])  # 15
print(my_list[-1])  # 17.5
print(my_list[-2])  # 28
# print(my_list[8])  # IndexError нет восьмого индекса

my_tuple = (15, 43, 425, "apple", 9.5)  # tuple (*кортеж)
print(my_tuple[0])  # 15
print(my_tuple[-1])  # 9.5

my_set = {34, 545, 4.23, "banana", 34}  # set (*множество)
print(my_set)  # {34, 545, 4.23, "banana"}
# print(my_set[0])  # ошибка. у множеств индекса нет


week = {  # dict (*словарь)
    1: "понедельник",
    2: "вторник",
    3: "среда",
    4: "четверг",
    5: "пятница",
}
print(week[3])  # среда

capitals = {
    "Кыргызстан": "Бишкек",
    "Франция": "Париж",
}
print(capitals["Франция"])  # Париж


# Функции
print("Hello everybody!")

number_str = input("введите любое число")  # str - тип строка
number = int(number_str)  # int - тип интеджер
print(number)  # любое число которое введет пользователь

number2_str = str(number2)
print(number2_str)  # "123.8"


digit = 7
digit = digit - 5
print(digit)  # 2