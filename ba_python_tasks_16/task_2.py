# Create your own implementation of a built-in function range, named in_range(), which takes three parameters:
# 'start', 'end', and optional step. Tips: See the documentation for 'range' function.

def in_range(start, end, optional_step):
    """My own implementation of a built-in function range."""
    # захист від передачі даних у вигляді str, що не є цифрою
    if str(start).isalpha() or str(end).isalpha() or str(optional_step).isalpha():
        print('Дані мають бути у числовому вигляді!')

    # переведення рядкових даних у разі їх передачі у цифру
    else:
        func_start = int(str(start))
        func_end = int(str(end))
        func_optional_step = int(str(optional_step))

        # перевірка двох некоректних умов передачі цифрових даних
        if (func_start > func_end) and (func_optional_step > 0):
            print(f'Некоректні дані. Перше число ({func_start}) більше останнього ({func_end}) '
                  f'при додатньому кроці ({func_optional_step}).')
        elif (func_start < func_end) and (func_optional_step < 0):
            print(f'Некоректні дані. Перше число ({func_start}) менше останнього ({func_end}) '
                  f'при від\'ємному кроці ({func_optional_step}).')

        # генерування списку у ситуації, коли всі дані введені коректно
        else:
            i = func_start
            while abs(i) < abs(func_end):
                yield i
                i += func_optional_step


# перевірка генерації списку у чотирьох випадках

# 1) перше число менше за друге, крок додатній (норма)
my_list_1 = in_range(100, 120, 3)
for num in my_list_1:
    print(f'Число з першого випадку — {num}')
print()

# 2) перше число більше за друге, крок додатній (попередження про неможливість розрахунку)
my_list_2 = in_range(120, 100, 3)
for num in my_list_2:
    print(f'Дані з другого випадку — {num}')
print()

# 3) перше число менше за друге, крок від'ємний (попередження про неможливість розрахунку)
my_list_3 = in_range(-100, 120, -3)
for num in my_list_3:
    print(f'Дані з третього випадку — {num}')
print()

# 4) перше число більше за друге, крок від'ємний (норма)
my_list_4 = in_range(100, -120, -3)
for num in my_list_4:
    print(f'Дані з четвертого випадку — {num}')
print()
