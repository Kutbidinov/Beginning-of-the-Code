# Пользователь вводит два числа.
# Программа должна напечатать либо:
# "первое число больше второго"
# либо "числа равны"
# либо "первое число меньше второго"

number1 = int(input('введите первое число'))
number2 = int(input('введите второе число'))

if number1 > number2:
    print('первое число больше второго')
elif number1 == number2:
    print('числа равны')
else:
    print('первое число меньше второго')