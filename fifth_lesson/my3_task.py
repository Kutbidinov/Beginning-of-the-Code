# мы можем с помощью for проходиться по листу, кортежу, множеству и словарю
my_list = [10, 20, 30, 40, 50]

# for i in my_list:
#     print(i)


# задача вывести таблицу умножения
number = int(input('введите число:'))

for i in range(1, 10):
    print(number, "x", i, "=", number * i)