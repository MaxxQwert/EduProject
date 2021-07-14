"""
- написать функцию, которая принимает N целых чисел и возвращает список квадратов эих чисел. Бонусом будет сделать
keyword аргумент для выбора степени, в которую будут возводиться числа
- написать функцию, которая на вход принимает список из целых чисел, и возвращает только чётные/нечётные/простые
числа (выбор производится передачей дополнительного аргумента)
- создать декоратор для замера времени выполнения функции
"""

import time


def timers(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        if len(args) == 1:
            typ = 'even'
        else:
            typ = args[1]
        print(f'Execution time of a function with an argument \'{typ}\' : {end - start} секунд.')
        return return_value

    return wrapper


def is_prime(mum):
    if mum <= 2:
        return False
    return all(mum % i for i in range(2, mum))


def degree_of_numbers(numbers, degree=2):
    return list(map(lambda x: x ** degree, numbers))


@timers
def even_odd_prime(numbers, typ='even'):
    if typ == 'even':
        return list(filter(lambda x: x % 2 == 0, numbers))
    elif typ == 'odd':
        return list(filter(lambda x: x % 2 != 0, numbers))
    elif typ == 'prime':
        return list(filter(is_prime, numbers))
    print(f'\'{typ}\' incorrect value')
    return 0


a = list(i for i in range(5000))
print(degree_of_numbers(a, 3))
print(even_odd_prime(a))
print(even_odd_prime(a, 'odd'))
print(even_odd_prime(a, 'prime'))
print(even_odd_prime(a, 'prme'))
