
class SmartHouse:

    def __init__(self, is_light_on_pm: bool, temperature_pm: int):
        self.is_light_on = is_light_on_pm  # включен ли свет
        self.__temperature = temperature_pm

    def get_temperature(self):  # геттер - метод который получает приватный атрибут
        return self.__temperature

    def set_temperature(self, temperature: int):  # сеттер - метод который устанавливает значение для приватного атрибута
        if temperature <= 40:
            self.__temperature = temperature

    def increase_temperature_by_one(self):
        self.__temperature += 1


dom = SmartHouse(is_light_on_pm=True, temperature_pm=25)

print(dom.is_light_on)
# print(dom.__temperature)  # AtributeError: данный атрибут является скрытым
print(dom.get_temperature())  # 25

dom.set_temperature(27)
print(dom.get_temperature())  # 27

dom.set_temperature(50)
print(dom.get_temperature())  # 27

dom.increase_temperature_by_one()
print(dom.get_temperature())  # 28


"""
Задание 4:
Для третьего задания сделайте атрибуты age и gender приватными.
Чтобы для age использовались только положительные 
а для gender только значения "M" и "Ж"
"""
