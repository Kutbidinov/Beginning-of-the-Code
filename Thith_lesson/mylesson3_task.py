
class Animal:  # родительский класс
    def __init__(self, name_pm: str, age_pm: int):
        self.name = name_pm
        self.age = age_pm


class Dog(Animal):  # дочерний класс

    def gav(self):
        print("ГАВ-ГАВ!")


class Cat(Animal):  # дочерний класс

    def meow(self):
        print("МЯУ)))))")


a1 = Dog("Рекс", 10)
a2 = Cat("Мурка", 20)
a3 = Dog("Мухтар", 30)

a1.gav()
a2.meow()
a3.gav()


class HomeDog(Dog):
    def __init__(self, name_pm: str, age_pm: int, owner_name_pm: str):
        self.name = name_pm
        self.age = age_pm
        self.owner_name = owner_name_pm

    def gav(self):
        print(f"ГАВ-ГАВ! моего хозяина зовут {self.owner_name}")


hd1 = HomeDog("Бетховен", 20, "Вася")
print(hd1.owner_name)  # Вася

hd1.gav()


"""
Задание 3:
Создайте класс Person с атрибутами name, age, gender. И метод introduce (в котором человек должен представиться .)
 Создайте класс Student унаследовав от класса Person.
 и добавьте для класса Student дополнительный атрибут course. (*на каком курсе учится)
 Создайте класс GraduatedStudent и измените метод introduce. (*привет меня зовут ... Я выпускник)
"""
