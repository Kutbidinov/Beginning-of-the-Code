number_list = [10, 30, 20, 500, 77]

maximum = 0
for number in number_list:
    if number > maximum:
        maximum = number
# 1-круг:number = 10. maximum=0
# 2-круг: number = 30 maximum = 10
# 3-круг: number = 20 maximum = 30
# 4-круг:number = 500 maximum = 30
# 5-круг: number = 77 maximum = 500

print(maximum)