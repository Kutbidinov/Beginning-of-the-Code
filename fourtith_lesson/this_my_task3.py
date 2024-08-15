
NUMBER_PI = 3.14159


def calculate_circle_area(radius: float, pi: float = NUMBER_PI) -> float:
    """Вычисляет площадь окружности."""
    area = pi * radius ** 2
    return area


def calculate_circle_length(radius: float) -> float:
    """Вычисляет длину окружности."""
    length = 2 * NUMBER_PI * radius
    return length


# calculate_circle_area(4)
# calculate_circle_area(radius=3)


# DRY - dont repeat yourself


def run_first_program(name: str = "World"):
    print(f"Hello {name}!")


run_first_program("Toktosun")
run_first_program()


# def sum_all_numbers(a, b, c):
#     return sum([a, b, c])


def improved_sum_all_numbers(*args):
    print(f'значения {args}')
    return sum(args)


# print(improved_sum_all_numbers(4, 9, 2))
# print(improved_sum_all_numbers(1, 2, 3, 64, 43, 64, 23))


def calculate_sum_two_number(a, b):
    return a + b


calculate_sum_two_number(3, 4)  # 7


def calculate_sum_by_number_list(number_list):
    return sum(number_list)


calculate_sum_by_number_list(number_list=[1,2,3])  # 6


def calculate_sum_by_numbers(*args):
    return sum(args)


calculate_sum_by_numbers(1, 2, 3, 4, 5)
"""
Задание:
 напишите функцию которая может принимать несколько аргументов
 и находить их произведение

 calculate_numbers_multiplications(2, 3)  # 6
 calculate_numbers_multiplications(2, 3, 2)  # 12
 calculate_numbers_multiplications(2, 3, 2, 2)  # 24
"""


def calculate_numbers_multiplications(*args):
    # args - это обычный кортеж из чисел
    total_multiplication = 1
    for item in args:
        total_multiplication = total_multiplication * item

    return total_multiplication


print(calculate_numbers_multiplications(2, 3))  # 6
print(calculate_numbers_multiplications(2, 3, 3))  # 18
print(calculate_numbers_multiplications(2, 3, 3, 2))  # 36


def print_counting_translations(first, second, third, **kwargs):
    # kwargs - key with arguments
    print(f"1. {first}")
    print(f"2. {second}")
    print(f"3. {third}")
    print(f"аргс {kwargs}")


print_counting_translations(first="биринчи", second="экинчи", third="учунчу", fourth="тортунчу", fifth="бешинчи")





capitals1 = {"Россия": "Москва", "Кыргызстан": "Бишкек"}

capitals2 = {"Франция": "Париж", "Италия": "Рим"}


capitals3 = {**capitals1, **capitals2}

print(capitals3)
