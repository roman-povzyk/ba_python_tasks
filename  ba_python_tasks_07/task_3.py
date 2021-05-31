def make_operation(operation, *args):
    if operation != '+' and operation != '-' and operation != '*':
        result = "Ви ввели невірний оператор: потрібно '+', '-' або '*'"
    else:
        result = args[0]
        for i in range(1, len(args)):
            if operation == '+':
                result += args[i]
            elif operation == '-':
                result -= args[i]
            else:
                result *= args[i]
    return result


print(make_operation('+', 7, 7, 2))
print(make_operation('-', 5, 5, -10, -20))
print(make_operation('*', 7, 6))
