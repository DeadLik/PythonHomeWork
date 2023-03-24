# Дана строка (возможно, пустая), состоящая из букв A-Z:
#
# AAAABBBCCXYZDDDDEEEFFFAAAAAABBBB
# BBBBBBBBBBBBBBBBBBBBBBBB
#
# Нужно написать функцию RLE,
# которая на выходе даст строку вида:
#
# A4B3C2XYZD4E3F3A6B28
#
# И сгенерирует ошибку, если на вход пришла
# невалидная строка.
#
# Пояснения: Если символ встречается 1 раз,
# он остается без изменений; Если символ
# повторяется более 1 раза, к нему
# добавляется количество повторений.

def RLE(s):
    if not s.isalpha():
        raise ValueError('Неверный Ввод: строка должна состоять только из букв алфавита')
    if not s:
        return ''
    res = []
    curr_char = s[0]
    curr_count = 1
    for i in range(1, len(s)):
        if s[i] == curr_char:
            curr_count += 1
        else:
            res.append(curr_char + str(curr_count))
            curr_char = s[i]
            curr_count = 1
    res.append(curr_char + str(curr_count))
    return ''.join(res)


s = 'AAAABBBCCXYZDDDDEEEFFFAAAAAABBBB'          # Верный формат
print(RLE(s))

s = 'BBBBBBBBBBBBBBBBBBBBBBBB123'           # Генерация ошибки
print(RLE(s))
