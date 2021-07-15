from typing import Optional


def to_power(x: Optional[float], exp: int) -> Optional[float]:
    """ Returns  x ^ exp """
    try:
        if exp >= 0:
            if exp == 1:
                return x
            else:
                return x * to_power(x, exp - 1)
        else:
            raise ValueError('This function works only with exp > 0.')
    except ValueError as err:
        return print(err)


print(to_power(2, 3))
print(to_power(3.5, 2))
print(to_power(2, -1))
