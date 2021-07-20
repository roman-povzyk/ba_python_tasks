# Extend the Queue to include a method called get_from_stack that searches
# and returns an element e from a queue. Any other element must remain in the queue
# respecting their order. Consider the case in which the element is not found
# - raise ValueError with proper info Message


class Queue:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return bool(self._items)

    def enqueue(self, item):
        self._items.insert(0, item)

    def dequeue(self):
        return self._items.pop()

    def size(self):
        return len(self._items)

    def get_from_stack(self, number):
        try:
            if len(self._items) - 1 < number:
                raise ValueError(f'Не можемо знайти елемент №{number}.')
            else:
                element = self._items[number]
                return element
        except ValueError as err:
            print(err)

    def __repr__(self):
        representation = "<Queue>\n"
        for ind, item in enumerate(reversed(self._items), 1):
            representation += f"{ind}: {str(item)}\n"
        return representation

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    q = Queue()
    q.enqueue(4)
    q.enqueue('dog')
    q.enqueue(True)
    print(q.size())
    print(q)
    print(q.get_from_stack(2))
