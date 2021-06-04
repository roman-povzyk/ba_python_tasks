# Write a function called oops that explicitly raises
# an IndexError exception when called.
# Then write another function that calls oops inside a try/except
# statement to catch the error.
# What happens if you change oops
# to raise KeyError instead of IndexError?


def oops():
    raise IndexError('У вас виникла IndexError')


def another_function():
    try:
        oops()
    except IndexError as err_text:
        print(f'{err_text}')


print(another_function())
