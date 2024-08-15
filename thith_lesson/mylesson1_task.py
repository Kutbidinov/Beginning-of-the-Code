
class Car:

    def __init__(self, mark_pm: str, model_pm: str, year_pm: int):
        self.mark = mark_pm
        self.model = model_pm
        self.year = year_pm


car1 = Car("BMW", "M8", 2020)
car2 = Car("Mercedes", "E200", 2024)

print(car1.mark)  # "BMW"
print(car2.mark)  # "Mercedes"

print(car2.model)  # "E200"

print(car1.year)  # 2020
car1.year = 2023
print(car1.year)  # 2023

"""
Задание: создайте класс Fruit с атрибутами color, name, price и тд 
Создайте конкретные фрукты: банан, яблоко, апельсин.
Напечатайте их атрибуты. Поменяйте цену для созданного яблока
"""

# примечание: мы также можем добавлять новые атрибуты для созданного объекта
car1.volume = 3.5

print(car1.volume)  # 3.5
# print(car2.volume)  # AtributeError: нет такого атрибута у объекта car2
