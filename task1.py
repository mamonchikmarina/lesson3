"""
Задача 16
Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
Пользователь в первой строке вводит натуральное число N – количество элементов в
массиве. В последующих строках записаны N целых чисел Ai. Последняя строка содержит
число X.
"""

from random import randint
M = 10
List_1 = [0] * M
for i in range (M):
    List_1[i] = randint(1, 50)
print(List_1)
N = int(input('Введите число N из списка = '))
res = 0
for i in range(len(List_1)):
    if List_1[i] == N:
        res += 1
print(res)


