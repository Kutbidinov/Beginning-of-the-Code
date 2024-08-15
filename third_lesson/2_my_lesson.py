# Примитивные типы: int, float, bool, str

# Структуры данных:

# Листы (*списки)
my_list = []  # list (*на русском список)
fruits = ["apple", "banana", "orange"]
number = [12, 54.32, 78]
values = ["Bishkek", 123, 7948, 54.3, number]

print(fruits[0])  # apple
print(fruits[2])  # orange

# # print(fruits[3])  # будет ошибка IndexError

print(fruits[-1])  # orange


numbers = (1, 5, 60, 70)  # tuple (*кортеж)
number[1]  # 5
number[-1]  # 70
number[0]  # 1


# чем отличается кортеж от листа? ответ: кортеж неизменяемый, лист изменяемый
my_list1 = [1, 2, 3]
my_list1.append(4)
print(my_list1)

my_tuple1 = (1, 2, 3)
# my_tuple1.append(4)  # AttributeError: 'tuple' object has no attribute 'append'
print(my_tuple1)

# структура данных - Set (*на русском множество)
my_set1 = {1, 2, 3, 2, 3, 3, 1, 2}
print(my_set1)

# структура данных - dict (*на русском словарь)
my_dict = {"hello": "привет", "bye": "пока"}
print(my_dict["hello"])