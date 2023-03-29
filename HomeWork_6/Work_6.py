# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
"""
first = int(input('input first element: '))
differ = int(input('difference element: '))
last  =int(input('total element: '))

list_1 = []
for elem in range(last):
   elem = first + elem*differ
   print(elem, end='; ')
"""

# Нахождение n-го члена арифметической прогрессии
"""
first = int(input('input first element: '))
differ = int(input('difference element: '))
num = int(input('position element: '))
num_n = first + (num-1)*differ
print(f'element on {num} position = {num_n}')
"""

# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint
def create(size):
    list_1 = [randint(-5, 9) for _ in range(size)]
    return list_1

def index(my_list):
    min_elem = int(input("input the first elements of the range: "))
    max_elem = int(input("input the second elements of the range:  "))
    for i in range(len(my_list)):
        if my_list[i] >= min_elem and my_list[i] <= max_elem:
            print(i, end=" ")

print()
num_size = int(input("input number of elements array: "))
my_list = create(num_size)
print(my_list)
index(my_list)