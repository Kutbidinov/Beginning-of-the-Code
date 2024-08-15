def calculator(x, y, operator):
    if operator == "-":
        result = x - y
    elif operator == "+":
        result = x + y
    elif operator == "*":
        result = x * y
    elif operator == "/":
        result = x / y
    return result
total = calculator(8, 2, "/")
print(total)  # 4
total2 = calculator(x=10, y=5, operator="+")
print(total2)  # 15

# напишите свою функцию которая принимает список,
# и затем возвращает максимальный элемент в списке
def calculate_maximum(number_list):
    maximum = 0
    for number in number_list:
        if number > maximum:
            maximum = number

    return maximum

calculate_maximum([3,5,64,1])
calculate_maximum([3,5,42,64,1])
calculate_maximum([3,5,64,1])
calculate_maximum([31,5,64,1])
calculate_maximum([3,5,644,1])
calculate_maximum([3,75,64,1])
calculate_maximum([312,5,64,1])

calculate_maximum([1,2,10, 7])  # 10