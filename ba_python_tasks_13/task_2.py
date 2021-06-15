# Write a Python program to access a function inside a function
# (Tips: use function, which returns another function)

def double_number(y):
    return y * 2


def do_square(f):
    def resulting_func(x):
        try:
            return (f(x)) ** 2
        except TypeError:
            print(f'Введений некоректний аргумент {x} (можливо str). Перевірте його, будь ласка.')

    return resulting_func


result = do_square(double_number)
print(result(100))
