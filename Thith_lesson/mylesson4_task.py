
import math


class Rectangle:

    def __init__(self, side1_pm: int, side2_pm: int):
        self.side1 = side1_pm
        self.side2 = side2_pm

    def calculate_area(self) -> int:
        area = self.side1 * self.side2
        return area


r1 = Rectangle(side1_pm=20, side2_pm=10)

r1_area = r1.calculate_area()
print(r1_area)  # 200


# Отличие методов от функций
# number_list = [10, 20, 30]
#
# print(len(number_list))  # 3
#
# number_list.append(40)
# number_list.sort()


class Triangle:

    def __init__(self, side1_pm: int, side2_pm: int, side3_pm: int):
        self.side1 = side1_pm
        self.side2 = side2_pm
        self.side3 = side3_pm

    def calculate_perimeter(self):
        perimeter = self.side1 + self.side2 + self.side3
        return perimeter

    def calculate_area(self):
        polu_perimeter = self.calculate_perimeter() / 2
        area = math.sqrt(polu_perimeter * (polu_perimeter - self.side1) * (polu_perimeter - self.side2) * (polu_perimeter - self.side3))
        return area


t1 = Triangle(3, 4, 5)


print("периметр равен ", t1.calculate_perimeter())  # 12

print("площадь равен ", t1.calculate_area())  # 6




"""
S = √p · (p — a)(p — b)(p — c)

a = 3
b = 4
c = 5

Perimeter = 12
poluperimeter = 6
S = √(6 * (6-3) * (6-4) * (6-5))
S = √(6 * 3 * 2 * 1)
S = √36
S = 6

"""

"""
Задание 2:
Напишите свой класс Circle. Напишите методы для вычисления площади окружности и метод для вычисления длины окружности.
Создайте окружность с радиусом 6. И напечатайте его длину окружности и площадь
"""

# Примечание
print(t1.side3)  # 5

# print(Triangle.side3)  # ERROR потому что у класса нету такого атрибута



# Полиформизм

figure_list = [Rectangle(5, 7), Triangle(3, 4, 5), Rectangle(8, 2)]


total_area_sum = 0
for item in figure_list:
    item_area = item.calculate_area()
    total_area_sum += item_area

print(total_area_sum)
