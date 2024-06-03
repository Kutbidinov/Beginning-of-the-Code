
from math import sqrt

# print(sqrt(64))  # 8

NUMBER_PI = 3.14159


def calculate_circle_square(radius):
    """Высчитывает площадь окружности по радиусу"""
    result = NUMBER_PI * (radius ** 2)
    return result


def calculate_circle_square_by_diameter(diameter, number2=0):
    """Высчитывает площадь окружности по диаметру"""
    print(number2)
    result = NUMBER_PI * ((diameter / 2) ** 2)
    return result


square1 = calculate_circle_square(10)
square2 = calculate_circle_square(radius=7)

square3 = calculate_circle_square_by_diameter(8)

# print(square1)
# print(square2)


# word = "Всем привет!\nВсем салам!"
# word2 = """
# Всем привет!
#
# Всем салам!
# """
# print(word2)


def squar(number, stepen=2):
    result = number ** stepen
    return result


print(squar(2, 2))  # 4
print(squar(2))  # 4
print(squar(2, 3))  # 8
