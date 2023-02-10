# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

def summa(a, b):
    if b == 0:
        return a
    else:
        return summa(a + 1, b - 1)


number_A = int(input('Введите число A: '))
number_B = int(input('Введите число B: '))

if number_A < 0 or number_B < 0:
    number_A = abs(number_A)
    number_B = abs(number_B)

result = summa(number_A, number_B)
print(f'Сумма двух чисел A и B = {result}')

