"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию
"""
# Александр Сергеевич Пушкин 26.05.1799

day = '26.05'
year = '1799'

"""Пример из прошлого ДЗ"""

# year_born = input("В каком году родился Пушкин: ")
#
# while year_born != year:
#     print('Неверный год! ')
#     year_born = input("В каком году родился Пушкин: ")
# print('Верный год!')
#
# day_born = input("В какой день родился Пушкин: ")
#
# while day_born != day:
#     print('Неверная дата!')
#     day_born = input("В какой день родился Пушкин: ")
# print('Все верно!')

"""Решение:"""

def f(x):
    if x == year:
        return print('Верный год')
    elif x != year:
        print('Неверный год!')
        input('В каком году родился Пушкин: ')
f(input('В каком году родился Пушкин: '))

def f(y):
    if y == day:
        return print('Верно')
    elif y != day:
        print('Неверно: ')
        input('Введите день: ')
f(input('Введите день: '))
print('Все верно! ')

"""Пример из видеообзора"""

# def questions_date(questions, date):
#     answer = input(questions)
#     while answer != date:
#         print('Неверно!')
#         answer = input(questions)
#
# questions_date('Введите год рождения Пушкина: ', '1799')
# questions_date('Введите день рождения Пушкина: ', '26.05')
# print('Верно!')






