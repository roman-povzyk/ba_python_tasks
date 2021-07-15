def sum_of_digits(digit_string: str) -> int:
    try:
        if digit_string.isdigit():
            if len(digit_string) == 1:
                return int(digit_string)
            else:
                first_digit = digit_string[0]
                return int(first_digit) + sum_of_digits(digit_string[1:])
        else:
            raise ValueError("input string must be digit string")
    except ValueError as err:
        print(err)


print(sum_of_digits('26'))
print(sum_of_digits('1054'))
print(sum_of_digits('test'))
