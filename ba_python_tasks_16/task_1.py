# Create your own implementation of a built-in function enumerate,
# named 'with_index', which takes two parameters: 'iterable' and
# 'start', default is 0. Tips: see the documentation for the enumerate function.

import itertools


def with_index(wi_iterable, wi_start=0):
    """My own implementation of a built-in function enumerate"""
    if str(wi_start).isalpha():
        print('Початкове значення потрібно ввести цифрою!')
    else:
        my_list = list(zip(itertools.count(start=int(str(wi_start))), wi_iterable))
        return my_list


2

fruits = ('apple', 'banana', 'cherry')
with_index_fruits = with_index(fruits, 1)
print(with_index_fruits)
