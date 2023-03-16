# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.
# Попробуйте использовать метод count(), а также решите задачу с помощью своего алгоритма (без count).
# Замерьте время работы двух алгоритмов и сравните, подумайте, почему оно отличается.
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     3
#     -> 1

import time


def count_element(lst, x):
    return lst.count(x)


def count_element_manual(lst, x):
    count = 0
    for i in lst:
        if i == x:
            count += 1
    return count


n = int(input("Введите количество элементов в массиве: "))
lst = list(map(int, input("Введите элементы массива через пробел: ").split()))
x = int(input("Введите число, которое нужно найти: "))

start_time = time.time()
count1 = count_element(lst, x)
end_time = time.time()
print(f"Количество вхождений элемента {x} в массиве: {count1}")
print(f"Время выполнения метода count(): {end_time - start_time:.8f} секунд")

start_time = time.time()
count2 = count_element_manual(lst, x)
end_time = time.time()
print(f"Количество вхождений элемента {x} в массиве: {count2}")
print(f"Время выполнения алгоритма без использования метода count(): {end_time - start_time:.8f} секунд")
