# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
#
# Пример:
# 4 4 -> 2 2
# 5 6 -> 2 3

sum_two_numbers = int(input('Введите сумму чисел: '))
product_two_numbers = int(input('Введите произведение чисел: '))

for natural_number_x in range(1, sum_two_numbers):
    natural_number_y = sum_two_numbers - natural_number_x
    if natural_number_x * natural_number_y == product_two_numbers:
        print(f'Два загаданных числа {natural_number_x} и {natural_number_y}')
        break
else:
    print('Такие числа не найдены.')
