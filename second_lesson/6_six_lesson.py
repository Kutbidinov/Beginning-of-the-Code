number = 10

# 1 способ
if number >= 0:
    if number == 0:
        print('число равен нулю')
    else:
        print("положительное число")
else:
    print('Отрицательное число')

# 2 способ
if number > 0:
    print("положительное число")
if number == 0:
    print('число равен нулю')
else:
    print('Отрицательное число')