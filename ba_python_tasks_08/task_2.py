# Write a function that takes in two numbers
# from the user via input(), call the numbers
# a and b, and then returns the value of squared
# a divided by b, construct a try-except block
# which raises an exception if the two values
# given by the input function were not numbers,
# and if value b was zero (cannot divide by zero).

def a_b_function():
    while True:
        a = input('Введіть число a: ')
        b = input('Введіть число b: ')
        try:
            d = int(a) ** 2 / int(b)
        except ValueError:
            print('Ви маєте ввести числові значення a та b')
        except ZeroDivisionError:
            print('Значення b не може дорівнювати 0')
        else:
            return d


print(a_b_function())
