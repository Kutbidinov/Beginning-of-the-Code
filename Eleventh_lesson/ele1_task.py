s
class Animal:

    def __init__(self, name_pm: str, age_pm: int):
        self.name = name_pm
        self.age = age_pm

    def run(self):
        print("я бегу")

    def voice(self):
        print("меня зовут", self.name)


class Dog(Animal):
    """класс собаки"""

    def voice(self):
        print("ГАВ!")
        print("меня зовут", self.name)


class Cat(Animal):
    """класс кошки"""

    def voice(self):
        print("МЯУ!")
        print("меня зовут", self.name)


cat1 = Cat(name_pm="Киса", age_pm=12)
dog1 = Dog(name_pm="Рекс", age_pm=12)

# cat1.run()
# dog1.run()

cat1.voice()
dog1.voice()

