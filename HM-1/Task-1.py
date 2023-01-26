# Найдите сумму цифр трехзначного числа.
# Пример:

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = input("Введите трёхзначное число: ")

if len(number) == 3 and number.isdigit():
    summa = int(number[0]) + int(number[1]) + int(number[2])
    print(f'Сумма цифр числа {number} = {summa}')
else:
    print('Неверное число')




