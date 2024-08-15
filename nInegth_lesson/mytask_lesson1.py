
number1 = 5
number2 = 3
print(number1 + number2)  # 8


string1 = "5"
string2 = "3"
print(string1 + string2)  # "53"

# print(number1 + string2)  TypeError

def calculate_multiplication(number1: int, number2: int) -> int:
    """Высчитывает произведение интежеров"""
    result = number1 * number2
    return result

# print(calculate_multiplication(3, 4))  # 12
# print(calculate_multiplication(3, "some"))


def print_one_hundred_times(word: str) -> None:
    for i in range(1, 101):
        print(word)


print_one_hundred_times("Салам!")
