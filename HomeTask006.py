###############################
### |ДЗ 04.06.2023 СЕМИНАР| ###
###############################
# ПОДКЛЮЧАЕМЫЕ БИБЛИОТЕКИ:
import random # подключение библиотеки для функционирования random.randint(0, 10)

#####################################################
"""
Задача 30:  Заполните массив элементами Арифметической прогрессии.
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
"""

# a1 = int(input("Введите первый элемент арифметической прогрессии: "))
# d = int(input("Введите разность арифметической прогрессии: "))
# n = int(input("Введите кол-во элементов арифметической прогрессии: "))

# list_1 = [a1 + i * d for i in range(n)]
# print(*list_1)

#####################################################

#####################################################
"""
Задача 32: Определить индексы элементов массива (списка), 
значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)
"""

# n_min = 5 # int(input("Введите Минимально число: "))
# n_max = 10 # int(input("Введите Максимальное число: "))

# list_1 = [random.randint(0, 15) for i in range(n_min + n_max)]
# print(list_1)
# for i in range(len(list_1)):
#   if list_1[i] >= n_min and list_1[i] <= n_max:
#     print(f"{list_1[i]}[{i}]", end=" ")

#####################################################