###############################
### |ДЗ 03.06.2023 СЕМИНАР| ###
###############################
# ПОДКЛЮЧАЕМЫЕ БИБЛИОТЕКИ:


#####################################################
"""
Задача 26: Напишите программу, которая на вход принимает два числа A и B,
и возводит число А в целую степень B с помощью рекурсии.
*Пример:*
A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8 
"""

# def Exponentiation(a, b):
#   if b == 0:
#      return 1
#   else:
#     return a * Exponentiation(a, b - 1)

# a = int(input("Укажите число: "))
# b = int(input("Укажите степень: "))
# print(Exponentiation(a, b))

#####################################################

#####################################################
"""
Задача 28: Напишите рекурсивную функцию sum(a, b),
возвращающую сумму двух целых неотрицательных чисел.
Из всех арифметических операций допускаются только +1 и -1.
Также нельзя использовать циклы.
*Пример:*
2 2
    4
"""

# def Sum(a, b):
#   # print("a=", a, "b=", b)
#   # print("a - 1=", a - 1,"||", "b + 1=", b + 1)
#   if a == 0:
#     return b
#   elif b == 0:
#     return a
#   else:
#     return Sum(a - 1, b + 1)

# a = int(input("Укажите первое число: "))
# b = int(input("Укажите второе число: "))
# print(Sum(a, b))

#####################################################