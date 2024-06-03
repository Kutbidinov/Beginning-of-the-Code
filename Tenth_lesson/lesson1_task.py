
class Car:
    def __init__(self, color_pm, speed_pm, model_pm):
        self.color = color_pm
        self.speed = speed_pm
        self.model = model_pm


# метод __init__ - конструктор
# color - атрибут
# self - будущий объект

bmw = Car(color_pm="синий", speed_pm=320, model_pm="BMW M5")
merc = Car(color_pm="чёрный", speed_pm=370, model_pm="Mercedes-Benz E210")

print(bmw.color)  # синий

distance = 1000

time_hours = distance / bmw.speed
print(time_hours)  # 3.125
 # Задание:
# Создайте класс `Country` с атрибутами (*сами придумайте)
# и создайте свои конкретные страны


class Country:

    def __init__(self, name_pm, area_pm, population_pm):
        self.name = name_pm
        self.area = area_pm
        self.population = population_pm


kyrgyzstan = Country(name_pm="Кыргызстан", area_pm=123, population_pm=7_000_000)
china = Country(name_pm="Китай", area_pm=321, population_pm=2_500_000_000)
# 7000000 == 7_000_000  # True

total_population = kyrgyzstan.population + china.population

print(total_population)


# number_list = [1,2,3]
# number_list.append(4)
# print(number_list)   # [1,2,3,4]
#
# sum(number_list)  # 10
