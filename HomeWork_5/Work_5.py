# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в
# целую степень B с помощью рекурсии.
"""
def expon(num, step):
    if step == 0:
        return 1
    else:
        return expon(num, step-1) * num
num = int(input('Введите число для возведения в степень: '))
step = int(input('Введите степень числа: '))
print(f'{num} ** {step} = {expon(num, step)}')
"""

# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.


def sumNum(num1, num2):
    if num1 == 0:
        return num2
    else:
        return sumNum(num1 - 1, num2 + 1)


sum1 = int(input('Введите 1-е число: '))
sum2 = int(input('Введите 2-е число: '))
print(f'{sum1} + {sum2} = {sumNum(sum1, sum2)}')
