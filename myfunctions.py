"""
МОДУЛЬ 1
В модуле прописаны заготовки для 8 функций
Под каждой функцией есть описание как она должна работать
ниже есть примеры использования функции
Задание: реализовать код функции, чтобы он работал по описанию и примеры использования давали верный результат
"""

# Задача 1
"""
Функция создает красивый резделитель из 10-и звездочек (**********)
:return: **********
"""
#
def simple_separator():
    return '*' * 10

p = simple_separator()
print('1 Задача: ')

print(list(p))
print(simple_separator() == '**********')  # True



# Задача 2
"""
Функция создает разделитель из звездочек число которых можно регулировать параметром count
:param count: количество звездочек
:return: строка разделитель, примеры использования ниже
"""

def long_separator(count):
    return '*' * count
print()
print('2 Задача: ')

print(long_separator(3))
print(long_separator(3) == '***')  # True

print(long_separator(4))
print(long_separator(4) == '****')  # True



# Задача 3
"""
    Функция создает разделитель из любых символов любого количества
    :param simbol: символ разделителя
    :param count: количество повторений
    :return: строка разделитель примеры использования ниже
    """

def separator(simbol, count):
    return simbol * count
print()
print('3 Задача: ')
print(separator('-', 10))
print(separator('-', 10) == '----------')  # True

print(separator('#', 5))
print(separator('#', 5) == '#####')  # True





# Задача 4
"""
Функция печатает Hello World в формате:
 **********
Hello World!
##########
:return: None
"""
'''
**********
Hello World!
##########
'''
print()
print('4 Задача: ')
def hello_world():

    print(separator(10, '*'), '\n')
    print('Hello World!', '\n')
    print(separator(10, '#'))
hello_world()

# Задача 5
"""
 Функция печатает приветствие в красивом формате
**********
Hello {who}!
##########
:param who: кого мы приветствуем, по умолчанию World
:return: None
"""
'''
**********
Hello World!
##########
'''
#hello_who()
'''
**********
Hello Max!
##########
'''
#hello_who('Max')
'''
**********
Hello Kate!
##########
'''
#hello_who('Kate')
print()
print('5 Задача: ')

def hello_who(who='World'):
    print(separator(10, '*'))
    print(f'Hello {who}!')
    print(separator(10, '#'))


hello_who()

hello_who('Max')

hello_who('Kate')

# Задача 6
"""
Функция складывает любое количество цифр и возводит результат в степень power (примеры использования ниже)
:param power: степень
:param args: любое количество цифр
:return: результат вычисления # True -> (1 + 2)**1
"""
print()
print('6 Задача: ')
def pow_many(power, *args):
    result = 0
    for number in args:
        result +=number
    return result ** power

print(pow_many(1, 1, 2))
print(pow_many(1, 1, 2) == 3)  # True -> (1 + 2)**1 == 3

print(pow_many(1, 2, 3))
print(pow_many(1, 2, 3) == 5)  # True -> (2 + 3)**1 == 5

print(pow_many(2, 1, 1))
print(pow_many(2, 1, 1) == 4)  # True -> (1 + 1)**2 == 4

print(pow_many(3, 2))
print(pow_many(3, 2) == 8)  # True -> 2**3 == 8

print(pow_many(2, 1, 2, 3, 4))
print(pow_many(2, 1, 2, 3, 4) == 100)  # True -> (1 + 2 + 3 + 4)**2 == 10**2 == 100







# Задача 7
"""
   Функция выводит переданные параметры в фиде key --> value
   key - имя параметра
   value - значение параметра
   :param kwargs: любое количество именованных параметров
   :return: None
   """
"""
name --> Max
age --> 21
"""

"""
animal --> Cat
is_animal --> True
"""
print()
print('7 Задача: ')

def print_key_val(**kwargs):
    for key, val in kwargs.items():
        print(key, '-->', val)


print_key_val(name='Max', age=21)
print()
print_key_val(animal='Cat', is_animal=True)


# Задача 7
"""
(Усложненое задание со *)
Функция фильтрует последовательность iterable и возвращает новую
Если function от элемента последовательности возвращает True, то элемент входит в новую последовательность иначе нет
(примеры ниже)
:param iterable: входнaя последовательность
:param function: функция фильтрации
:return: новая отфильтрованная последовательность
"""

print()
print('7 Задача: ')


def my_filter(iterable, function):
    result = []
    for x in iterable:
        if function(x):
            result.append(x)
    return(result)

print()
print(my_filter([1, 2, 3, 4, 5], lambda x: x > 3))
print(my_filter([1, 2, 3, 4, 5], lambda x: x > 3) == [4, 5])  # True

print(my_filter([1, 2, 3, 4, 5], lambda x: x == 2))
print(my_filter([1, 2, 3, 4, 5], lambda x: x == 2) == [2])  # True

print(my_filter([1, 2, 3, 4, 5], lambda x: x != 3))
print(my_filter([1, 2, 3, 4, 5], lambda x: x != 3) == [1, 2, 4, 5])  # True

print(my_filter(['a', 'b', 'c', 'd'], lambda x: x in 'abba'))
print(my_filter(['a', 'b', 'c', 'd'], lambda x: x in 'abba') == ['a', 'b'])  # True
