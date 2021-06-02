# Write a function called oops that explicitly raises
# an IndexError exception when called.
# Then write another function that calls oops inside a try/except
# statement to catch the error.
# What happens if you change oops
# to raise KeyError instead of IndexError?


def oops():
    raise IndexError('hello')


def another_function(x):
    try:
        print(x[4])
    except IndexError:
        oops()


print(another_function([1, 2, 3]))
