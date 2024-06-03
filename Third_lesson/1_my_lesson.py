# пользователь вводит сумму в сомах, например 1000.
# и вводит валюту, например евро или доллар
# программа перевед курс в доллар или евро

# курс 1 доллар это 88 сом
# курс 1 евро это 97 сом

som = int(input('введите сумму'))
currency = input("введите имя валюты")

dollar_curs = 88
euro_curs = 97

if currency == "евро":
    result = som / euro_curs
    print(result)
elif currency == "доллар":
    result = som / dollar_curs
    print(result)
else:
    print("неизвестная валюта")