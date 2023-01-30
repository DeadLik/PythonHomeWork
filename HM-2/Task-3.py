# Требуется вывести все целые степени двойки (т.е. числа вида 2k),
# не превосходящие числа N.
#
# Пример:
# 10 -> 1 2 4 8

number_n = int(input('Введите число N: '))

power_of_two = 1
while power_of_two <= number_n:
    print(power_of_two)
    power_of_two *= 2

