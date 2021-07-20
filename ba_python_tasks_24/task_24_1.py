# Write a program that reads in a sequence of characters
# and prints them in reverse order, using your implementation of Stack.

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


def reverse_sequence():
    input_sequence = input('Введіть свою фразу: ')
    our_stack = Stack()

    for symbol in input_sequence:
        our_stack.push(symbol)

    input_sequence_reverse = ''

    while our_stack.is_empty():
        input_sequence_reverse += our_stack.pop()

    return input_sequence_reverse


print(reverse_sequence())
