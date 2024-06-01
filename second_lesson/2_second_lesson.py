number = 5

if number > 3:
    print("больше 3")
elif number > 2:  # если number > 1 истина/правда то даже эту строку не проверит
    print("больше двух")
elif number > 1:
    print("больше одного")
else:
    print('иначе')
print('конец программы')