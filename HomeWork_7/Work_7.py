# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его
# кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения
# одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в
# порядке

"""
1 способ
def ritm(poem):
    let_gl = 'ауоыиэяюёе'
    List_let = []
    for word in poem:
        count = 0
        for letter in word:
            if letter in let_gl:
                count += 1
        List_let.append(count)
    return len(List_let) == List_let.count(List_let[0])


text_poem = 'пара парам парам'.lower().split()
print(text_poem)
if ritm(text_poem):
    print('Парам пам-пам')
else:
    print('Пам парам')
"""
# 2 способ

"""
def ritm(characteristic, objects):
    return len(set(map(characteristic, objects))) == 1

poem = 'пара-ра-рам рам-пам-папам па-ра-па-да'
poem_1 = poem.split()

if ritm(lambda x: sum(1 for i in x if i in "аоуыэеёиюя"), poem_1):
    print("Парам пам-пам")
else:
    print("Пам парам")
"""

# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в
# качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns
# указывают число строк и столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов идет с
# единицы (подумайте, почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.


def print_operation_table(operation, num_rows=6, num_cols=6):
    for i in range(1, num_rows + 1):
        for j in range(1, num_cols + 1):
            print(operation(i, j), end=" ")
        print()


print_operation_table(lambda rows, cols: rows * cols)
