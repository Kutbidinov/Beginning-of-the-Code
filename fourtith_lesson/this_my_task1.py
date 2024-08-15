
import random
from functools import lru_cache


@lru_cache()
def get_random_number():
    return random.randint(1, 101)


# print(get_random_number())
# print(get_random_number())
# print(get_random_number())


class Human:
    def __init__(self, name_pm: str, age_pm: int):
        self.name = name_pm
        if age_pm < 0:
            raise ValueError("Возраст не может быть отрицательным!")

        self.__age = age_pm

    @property
    def get_age(self):
        return self.__age

    def set_age(self, age: int):
        if age >= 0:
            self.__age = age


adam = Human(name_pm="Адам", age_pm=10)

print(adam.name)
print(adam.get_age)  # 10

adam.name = "Adam 2.0"

adam.set_age(20)
print(adam.get_age)  # 20


adam.set_age(-10)
print(adam.get_age)  # 20


eva = Human("Ева", -5)

# print(eva.get_age)  # -5

try:
    number = 5 / 0
except ZeroDivisionError:
    print("на нуль делить низя")
