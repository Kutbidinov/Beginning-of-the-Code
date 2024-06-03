
def calculate_sum_of_list(number_list: list):
    return sum(number_list)


def calculate_factorial(number: int) -> int:
    factorial = 1
    for i in range(1, number+1):
        factorial *= i  # factorial = factorial * i
    return factorial
