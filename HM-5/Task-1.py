# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии. >

def degree_b(a, b):
    if b == 0:
        return 1
    else:
        return a * degree_b(a, b - 1)


number_A = int(input('Введите число A: '))
number_B = int(input('Введите число B: '))

if number_A < 0 or number_B < 0:
    number_A = abs(number_A)
    number_B = abs(number_B)

result = degree_b(number_A, number_B)
print(f"A в степени B = {result}")
