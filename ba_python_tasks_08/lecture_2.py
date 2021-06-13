def my_func(x, y):
    if not y:
        raise ZeroDivisionError('На нуль ділити не можна!')
    z = x / y + 17
    return z


try:
    my_func(77, 0)
except ZeroDivisionError as error:
    print(f'Error inspected {error}')
except TypeError as error:
    print(f'Error inspected {error}')
except Exception:
    print('Щось пішло не так')
    raise
else:
    print('All Ok!')
finally:
    print('Цей блок виконається у будь-якому випадку')

# print(my_func(77, 0))
