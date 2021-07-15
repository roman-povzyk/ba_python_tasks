def mult(a: int, n: int) -> int:
    """ This function works only with positive integers """
    try:
        if n >= 0 and a >= 0:
            if n == 1:
                return a
            elif n == 0:
                return 0
            else:
                return a * mult(a, n-1)
        else:
            raise ValueError('This function works only with positive integers.')
    except ValueError or TypeError as err:
        print(err)


print(mult(2, 4))
print(mult(2, 0))
print(mult(2, -4))
