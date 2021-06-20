# Write a decorator that prints a function
# with arguments passed to it.

# NOTE! It should print the function, not the
# result of its execution!

# For example:
# 'add called with 4, 5'


def logger(func):
    def inside_func(*args, **kwargs):
        return f'{func.__name__} called with {args}'
    return inside_func


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


add_1 = add(4, 5)
print(add_1)
square_all_1 = square_all(1, 2, 3)
print(square_all_1)
