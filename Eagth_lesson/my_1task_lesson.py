
# sum([1, 2, 3])  # 6
# total_len = len("hello")  # 5
# print(total_len)  # 5
# max([5, 100, 8, 7])  # 100
#
# for i in range(5):
#     print(i)  # 0 - 4
#
# for i in range(1, 6):
#     print(i)  # 1 - 5
#
# for i in range(1, 6, 2):
#     print(i)  # 1 - 5 (c шагом 2: 1, 3, 5)

def calculate_chastnoe(x, y):
    if y == 0:
        print("на нуль делить нельзя")
        return None

    result = x / y
    # локальные переменные: x, y, result
    return result


chastnoe1 = calculate_chastnoe(10, 2) # 5
chastnoe2 = calculate_chastnoe(50, 5)  # 10
chastnoe3 = calculate_chastnoe(0, 7)  # 0
print("частное3", chastnoe3)  # 0

chastnoe4 = calculate_chastnoe(7, 0)
print("частное4", chastnoe4)  # None
