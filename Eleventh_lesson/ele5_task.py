
from ele2_task import calculate_sum_of_list, calculate_factorial

# тестируем функцию calculate_sum_of_list
assert calculate_sum_of_list([1, 2, 3]) == 6
assert calculate_sum_of_list([10]) == 10
assert calculate_sum_of_list([]) == 0
assert calculate_sum_of_list([-2, 1]) == -1

# тестируем функцию calculate_factorial
assert calculate_factorial(1) == 1
assert calculate_factorial(3) == 6
assert calculate_factorial(6) == 720
assert calculate_factorial(0) == 1
print(calculate_factorial(10))