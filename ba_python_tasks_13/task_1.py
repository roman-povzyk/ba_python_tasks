import random


def my_function_with_random_list():
    num_var = random.randint(1, 1000)
    list_var = []
    for i in range(num_var):
        list_var.append(i)
    return sum(list_var)


print(f'Загальна сума випадкових елементів у списку — {my_function_with_random_list()}.')
print(f'Загальна кількість локальний змінних у фунції — {my_function_with_random_list.__code__.co_nlocals}.')
