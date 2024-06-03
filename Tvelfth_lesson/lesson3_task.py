class SmartHouse:
    _d = "h"

    def __init__(self, temperature_pm: int, is_light_on_pm: bool):
        self.__temperature = temperature_pm
        self.is_light_on = is_light_on_pm

    def increase_temperature(self):
        if self.__temperature < 40:
            self.__temperature += 1


dom = SmartHouse(temperature_pm=39, is_light_on_pm=True)
print(dom.is_light_on)
print(dom.increase_temperature())