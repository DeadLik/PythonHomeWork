# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок,
# если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# Пример:
#
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

paper_crane = 60
petya_and_sergey = paper_crane // 6
katia = (paper_crane // 6) * 4

print(petya_and_sergey, katia, petya_and_sergey)



