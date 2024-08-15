
color_list = ["красный", "желтый", "зеленый", "черный", "белый"]
color_tuple = ("красный", "желтый", "зеленый")
word = "Kyrgyzstan"

print(color_list[1])  # желтый
print(color_tuple[1])  # желтый
print(word[2])  # r

print(color_list[1:3])  # ["желтый", "зеленый"]
print(color_list[:3])  # ["красный", "желтый", "зеленый"]
print(color_list[1:])  # ["желтый", "зеленый", "черный", "белый"]
print(color_list[1::3])  # ['желтый', 'белый']
print(color_list[::-1])  # ['белый', 'черный', 'зеленый', 'желтый', 'красный']

reversed_color_list = color_list[::-1]
print(reversed_color_list[0:5:2])

print(word[1:3])  # yr
