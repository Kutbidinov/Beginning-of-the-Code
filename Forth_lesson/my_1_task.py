# 1 способ
som = int(input('введите вашу сумму в сомах: '))

dollar_curs = 89.34
euro_curs = 96.92

currency = input("введите вашу валюту в которую перевести:")

if currency == "euro":
    result = som // euro_curs
    print(result)
elif currency == "dollar":
    result = som // dollar_curs
    print(result)
else:
    print('извините, я не знаю вашу валюту')


# 2 способ
my_dict = {
    "dollar": 89.34,
    "euro": 96.92,
}

som = int(input("введите вашу сумму в сомах: "))
currency = input("введите вашу валюту в которую перевести:")

currency_curs_value = my_dict[currency]
print("курс вашей валюты равен ", currency_curs_value)

result = som / currency_curs_value
print('результат равен', result)