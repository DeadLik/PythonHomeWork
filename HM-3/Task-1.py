# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению

import random

arrayLength = int(input('Введите длину списка: '))
arrayList = [random.randint(1, 100) for _ in range(arrayLength)]
# print(arrayList)
x = int(input('Введите искомое число: '))

count = 0
closest = arrayList[0]
closest_diff = abs(closest - x)
for num in arrayList:
    if num == x:
        count += 1
    elif abs(num - x) < closest_diff:
        closest = num
        closest_diff = abs(num - x)

if count == 0:
    print(f'Число {x} не найдено, ближайщее число к искомому {closest}')
else:
    print(f'Число {x} найдено, встречается {count} раз(а)')
