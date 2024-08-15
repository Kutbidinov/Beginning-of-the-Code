# for i in range(1, 10):
#     if i % 2 != 0:  # вернет True если число делится на нуль с остатком
#         continue
#     print('это число четное', i)

my_list = [1, 5, -9, 3]

for i in my_list:
    if i < 0:
        print('у нас есть отрицательно число')
        break