
class Human:
    def __init__(self, name_pm: str, age_pm: int, gender_pm: str):
        self.name = name_pm
        self.__age = age_pm
        self.gender = gender_pm

    def get_age(self):
        return self.__age

    def set_age(self, age: int):
        if age > 0:
            self.__age = age

    def introduce(self):
        print(f"Привет! Меня зовут {self.name}.")


# Human.introduce()  # ERROR: не можем вызывать ИЗ самого класса


class Student(Human):
    def __init__(self, name_pm: str, age_pm: int, gender_pm: str, course_pm: int):
        self.name = name_pm
        self.__age = age_pm
        self.gender = gender_pm
        self.course = course_pm

    def introduce(self):
        print(f"Привет! Я хороший студент! Атвечаю! Меня зовут {self.name}. ")

    def say_i_am_here(self):
        print("я здесь!")


class Teacher(Human):

    def increase_student_course(self, student_object: Student):
        # student_object.course += 1
        student_object.course = student_object.course + 1


class GraduatedStudent(Student):

    def graduation_speech(self):
        print("Спасибо универ что я окончил!")


person = Human(name_pm="Асан", age_pm=20, gender_pm="M")
person.introduce()

print(person.name)  # Асан
vozrast = person.get_age()
print(vozrast)  # 20

person.set_age(25)
print(vozrast)  # 20
print(person.get_age())  # 25

person.set_age(-10)
print(person.get_age())  # 25


shurik = Student("Александр", 20, "M", 1)
maria = Teacher("Мария Ивановна", 40, "Ж")

maria.increase_student_course(shurik)

"""
Напишите свой класс Сотрудника с методами имя, стаж работы и ЗП
И напишите метод которые изменяет заработную плату сотрудника
*учтите ЗП не может отрицательным

Создайте новый класс Manager.
 Менеджер может увеличивать ЗП сотрудника.
 Сотрудник уже не может увеличивать свою ЗП.
"""


class Employee(Human):
    def __init__(self, name_pm: str, age_pm: int, gender_pm: str, salary_pm: int):
        self.name = name_pm
        self.__age = age_pm
        self.gender = gender_pm
        self.__salary = salary_pm

    def get_salary(self) -> int:
        return self.__salary

    def set_salary(self, salary: float) -> None:
        if salary > 0:
            self.__salary = salary


class Manager(Human):

    def increase_employee_salary(self, employee_obj: Employee, increase_percent: int):
        new_employee_salary = self.__calculate_new_salary(
            current_salary=employee_obj.get_salary(),
            increase_percent=increase_percent,
        )
        employee_obj.set_salary(new_employee_salary)

    def __calculate_new_salary(self, current_salary, increase_percent: int):
        new_employee_salary = current_salary + (current_salary / 100 * increase_percent)
        return new_employee_salary


worker = Employee("Миша", 20, "M", 10_000)
print(worker.get_salary())  # 10000
sheff = Manager("Босс-молокосос", 40, "M")
sheff.increase_employee_salary(worker, 15)

print(worker.get_salary())  # 11500
