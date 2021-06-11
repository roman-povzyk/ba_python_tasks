# Create a Fraction class, which will represent all basic
# arithmetic logic for fractions (+, -, /, *)
# with appropriate checking and error handling

from decimal import Decimal


class Fraction:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if not isinstance(other, type(self)):
            raise ValueError('Невірний тип аргументу')
        return Fraction(self.value + other.value)

    def __sub__(self, other):
        if not isinstance(other, type(self)):
            raise ValueError('Невірний тип аргументу')
        return Fraction(self.value - other.value)

    def __mul__(self, other):
        if not isinstance(other, type(self)):
            raise ValueError('Невірний тип аргументу')
        return Fraction(self.value * other.value)

    def __truediv__(self, other):
        if not isinstance(other, type(self)):
            raise ValueError('Невірний тип аргументу')
        try:
            return Fraction(self.value // other.value)
        except ZeroDivisionError:
            return print('Другий аргумент, на який ділять — нуль!')

    def __str__(self):
        self.value = round(Decimal(self.value), 6).as_integer_ratio()
        if self.value[1] == 1:
            return f"Відповідь: {self.value[0]}"
        else:
            return f"Відповідь: {self.value[0]}/{self.value[1]}"

    def __repr__(self):
        return self.__str__()


x = Fraction(1 / 2)
y = Fraction(1 / 4)

print(x + y)
print(x - y)
print(x * y)
print(x / y)
