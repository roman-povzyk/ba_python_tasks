def reverse(input_str: str) -> str:
    """Function returns reversed input string """
    if len(input_str) == 1:
        return input_str
    else:
        last_letter = input_str[-1]
        return last_letter + reverse(input_str[:-1])


print(reverse("hello"))
print(reverse("o"))
