
class Person:

    def __init__(self, name_pm: str, age_pm: int):
        self.name = name_pm
        self.age = age_pm

    def ask_question(self, question_text: str):
        print(f"у меня вопрос: {question_text}")

    def answer_to_question(self, answer_text):
        print(f"мой ответ: {answer_text}")


class Student(Person):

    def say_here(self):
        print(f"меня зовут {self.name}! я здесь!")


class Teacher(Person):

    def say_attendance(self):
        print("кто сегодня присутствует?")

    def give_mark(self, student, mark):
        print(f"я ставлю {student.name} оценку {mark}")


nur = Student(name_pm="Нуржигит", age_pm=20)
asan = Student(name_pm="Асан", age_pm=30)

maria = Teacher(name_pm="Мария Ивановна", age_pm=40)
maria.give_mark(student=asan, mark=4)
maria.give_mark(student=nur, mark=5)

# maria.say_attendance()
# nur.say_here()
# asan.say_here()
#
# nur.ask_question("Что такое float?")
# asan.ask_question("Что такое ООП?")
#
# nur.answer_to_question("какой-то ответ на какой-то вопрос")
