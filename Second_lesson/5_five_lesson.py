number1 = 10
number2 = 2

print(number1 * number2)  # 20
print(number1 ** number2)  # 100 - возведение в степень
print(number1 / 2)  # 5.0
print(11 // 2)  # 5 - целочисленное деление
print(14 % 3)  # 2 - нахождение остатка


# операторы сравнения
print(number1 > number2)  # True
print(number1 < number2)  # False
print(number1 >= number2)  # True
print(number1 <= number2)  # False
print(number1 == number2)  # False
print(number1 != number2)  # True


if number1 > number2:
    print('номер 1 больше номера 2')
else:
    print('номер 1 не больше чем номер 2')

number1 = int(input("введите первое число"))
number2 = int(input("введите второе число"))

operator = input("введите ваш арифметический оператор: ")

if operator == "+":
    result = number1 + number2
elif operator == "-":
    result = number1 - number2
elif operator == "*":
    result = number1 * number2
elif operator == "/":
    if number2 != 0:
        result = number1 / number2
    else:
        print("нельзя делить на нуль")
        result = 0  # пока используем 0, потом будем `None`
else:
    print('я не знаю такого оператора')
    result = 0  # пока будем использовать нуль, потом со временем познакомлю вас с одним типом `None`

print("ваш результат равен", result)


# Логические операторы: and, or, in
number1 = 5
number2 = 2
if (number1 > number2) and (number1 == number2):
    # для and логического оператора нужно чтобы оба были True
    print("первое условие сработало")
elif (number1 > number2) or (number1 == number2):
    # для or логического оператора нужно чтобы хотя бы один из условий был True
    print("второе условие сработало")

my_list = [20, 55, 21, 7, 0, 65]

print(5 in my_list)  # False
print(7 in my_list)  # True

print(not (5 > 1))  # False
print(not (2 > 10))  # True

print(True and True)  # True
print(True and False)  # False
print(True or True)  # True
print(True or False)  # True