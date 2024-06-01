total_minute = int(input("введите общее количество минут: "))

hour = total_minute // 60  # часы
hour = hour % 24

minute = total_minute % 60

print('часы: ')
print(hour)

print('минуты:')
print(minute)