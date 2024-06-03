number1 = 100


try:
    number2 = int(input("введите число"))
    print('ваше число', number2)
except ValueError:
    print("СОРИ, вашу строку я не могу конвертировать в число")
# "555" -> 555
# "blablabla" -> ValueError

# 1 способ
# if number2 == 0:
#     print("на нуль делить низя")
# else:
#     chastnoe = number1 / number2
#
#     print(chastnoe)


# 2 способ
# try:
#     chastnoe = number1 / number2  # ZeroDivisionError - это ошибка может возникнуть
#     print(chastnoe)
# except ZeroDivisionError:
#     print("на нуль делить нельзя")