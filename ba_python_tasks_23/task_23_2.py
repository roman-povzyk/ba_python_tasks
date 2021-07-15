def is_palindrome(looking_str: str, index: int = 0) -> bool:
    """ Checks if input string is Palindrome """
    if len(looking_str) == 1:
        return True
    elif len(looking_str) == 2 and looking_str[0] == looking_str[-1]:
        return True
    else:
        if looking_str[0] == looking_str[-1]:
            return is_palindrome(looking_str[1:-1])
        else:
            return False


print(is_palindrome('mom'))
print(is_palindrome('sassas'))
print(is_palindrome('o'))
