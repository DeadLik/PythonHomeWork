# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
#
# *Пример:
# 5 -> 1 0 1 1 0
# 2

import random

n = int(input("Введите количество монет: "))
print()
eagle = 0
tails = 0

for _ in range(n):
    coins = random.randint(0, 1)
    if coins == 1:
        eagle += 1
    else:
        tails += 1

if eagle >= tails:
    print(f'Нужно перевернуть {tails}')
else:
    print(f'Нужно перевернуть {eagle}')

print()
print(f'количество орлов: {eagle}\nколичество решек: {tails}')