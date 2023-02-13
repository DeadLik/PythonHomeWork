# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

def find_indices_in_range(arr, minimum, maximum):
    return [i for i, n in enumerate(arr) if minimum <= n <= maximum]


arr = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
minimum = -5
maximum = 10
print(find_indices_in_range(arr, minimum, maximum))


