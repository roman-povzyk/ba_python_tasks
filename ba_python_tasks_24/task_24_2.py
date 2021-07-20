# Write a program that reads in a sequence of characters,
# and determines whether it's parentheses, braces,
# and curly brackets are "balanced."

class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return bool(self._items)

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[len(self._items) - 1]

    def size(self):
        return len(self._items)

    def __repr__(self):
        representation = "<Stack>\n"
        for ind, item in enumerate(reversed(self._items), 1):
            representation += f"{ind}: {str(item)}\n"
        return representation

    def __str__(self):
        return self.__repr__()


def balanced_symbols():
    input_sequence = input('Введіть свою фразу: ')
    our_stack = Stack()

    num_brackets_open = 0
    num_brackets_close = 0

    for symbol in input_sequence:
        our_stack.push(symbol)
        if symbol == '(' or symbol == '[' or symbol == '{':
            num_brackets_open += 1
        elif symbol == ')' or symbol == ']' or symbol == '}':
            num_brackets_close += 1

    if num_brackets_open == num_brackets_close:
        return 'balanced'
    else:
        return 'not balanced'


print(balanced_symbols())
