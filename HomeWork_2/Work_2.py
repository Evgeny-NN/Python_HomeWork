
# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
"""
import random
num = int(input('enter the number of coins: '))
figure = 0
embleme = 0
for i in range(num):
    number = random.randint(0, 1)
    print(number)
    if number == 1:
        figure += 1
    else:
        embleme += 1
if figure == embleme:
    print (f"Balance")
elif figure < embleme:
    print (f"Min figure = {figure}" )
else: print((f"Min figure = {embleme}" ))

"""

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по
# математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого
# Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать
# задуманные Петей числа.

"""
sum = int (input("Введите сумму чисел: "))
przv = int (input("Введите произведение чисел: "))
y = int((sum + ((-sum) ** 2 - 4 * przv) ** 0.5) / 2)
x = int((sum - ((-sum) ** 2 - 4 * przv) ** 0.5) / 2)
if sum == x + y and przv == x * y:
    print(x, y)
else:
    print ("No!")
"""

"""
# 2 способ (не эффективен по времени выполнения кода большим кол-м итераций)

sum = int(input("Summ =  "))
przv = int(input("Composition =  "))
for i in range(sum):
    for j in range(przv):
        if (sum == i + j and przv == i * j):
            print(i, j)
"""
# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

num = int(input("Введите целое число: "))
k = 1
print(end='[')
while 2 ** k <= num:
    print(k, end='-')
    k += 1
if 2**k >= num:
    print("]")
