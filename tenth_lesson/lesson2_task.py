
class Rectangle:

    def __init__(self, dlina_pm, shirina_pm):
        self.dlina = dlina_pm
        self.shirina = shirina_pm

    def calculate_square(self):
        result = self.dlina * self.shirina
        return result

    def calculate_perimeter(self):
        result = (self.dlina + self.shirina) * 2
        return result


r1 = Rectangle(dlina_pm=4, shirina_pm=5)
r2 = Rectangle(dlina_pm=15, shirina_pm=2)

square1 = r1.calculate_square()
perimeter1 = r1.calculate_perimeter()
# print(square1)  # 20
# print(perimeter1)  # 18


class Queue:  # переводится как "очередь"

    def __init__(self):
        self.data = []

    def put(self, name):
        self.data.append(name)

    def out(self):
        return self.data.pop(0)


q1 = Queue()
q1.put("бабушка Валя")
q1.put("дедушка Коля")
q1.put("дядя Вася")
q1.put("Петя")

print(q1.out())  # "бабушка Валя"

print(q1.out())  # "дедушка Коля"

q1.put("Асан")

print(q1.out())  # "дядя Вася"

print(q1.out())  # Петя
print(q1.out())  # Асан
print(q1.out())

