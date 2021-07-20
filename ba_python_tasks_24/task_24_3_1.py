# Extend the Stack to include a method called get_from_stack that searches and returns
# an element e from a stack. Any other element must remain on the stack respecting their order.
# Consider the case in which the element is not found - raise ValueError with proper info Message

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

    def get_from_stack(self, item):
        try:
            if item in self._items:
                return item
            else:
                raise ValueError(f'Не можемо знайти елемент.')
        except ValueError as err:
            print(err)

    def __repr__(self):
        representation = "<Stack>\n"
        for ind, item in enumerate(reversed(self._items), 1):
            representation += f"{ind}: {str(item)}\n"
        return representation

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    s = Stack()

    print(s.is_empty())
    s.push('Roma')
    s.push('Katya')
    s.push('Artem')
    s.push('Anna')
    print(s)
    print(s.get_from_stack('Artem'))
