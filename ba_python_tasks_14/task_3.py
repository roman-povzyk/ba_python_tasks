# Write a decorator `arg_rules` that validates arguments passed to the function.
# A decorator should take 3 arguments:
# max_length: 15
# type_: str
# contains: [] - list of symbols that an argument should contain
# If some of the rules' checks returns False, the function should
# return False and print the reason it failed;
# otherwise, return the result.

def arg_rules(type_: type, max_length: int, contains: list):
    def inside(func):
        def wrapper(func_arg):
            """Переписуємо поведінку нашої функції"""
            if type(func_arg) == type_ and len(func_arg) < 16:
                for element in contains:
                    if element in func_arg:
                        pass
                    else:
                        return False
                return func(func_arg)
            else:
                return False
        return wrapper
    return inside


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f'{name} drinks pepsi in his brand new BMW!'


print(create_slogan('johndoe05@gmail.com'))
print(create_slogan('S@SH05'))

