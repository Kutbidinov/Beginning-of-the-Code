
number_list = [1, 8, 4]
max_number = number_list[0]

for item in number_list:
    if item > max_number:
        max_number = item

# print(max_number)  # -1
name = input("введите свое имя")
surname = input("введите свою фамилию")


# greetings = "привет " + name + " " + surname
greetings = f"привет {name} {surname}"
print(greetings)
