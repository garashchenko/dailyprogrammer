from math import log, sqrt
from functools import lru_cache


def find_closest_fibonacci_index(num):
    alpha = (1 + sqrt(5)) / 2
    return int(log(sqrt(5) * num) / log(alpha))


@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


_fibs = []


def find_sum(num, result=[]):
    value = max(filter(lambda x: x <= num, _fibs))
    result.append(value)

    if num == value:
        return result
    num = num - value

    find_sum(num, result)
    return result


def construct_string(num):
    fibs_array = find_sum(num)
    joined_parts = ' + '.join(str(num) for num in fibs_array)
    return '%s = %s' % (num, joined_parts)


def get_input():
    try:
        number = int(input('Enter number: '))
    except ValueError:
        print('Wrong input!')
        return
    global _fibs
    _fibs = [fib(n) for n in range(number)]
    print(construct_string(number))