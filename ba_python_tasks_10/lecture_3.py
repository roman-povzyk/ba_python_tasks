class FirsrClass:
    class_attr = 0

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def do_something(self):
        print(f'A: {self.a}, B: {self.b}')
        return self.a + self.b

x = FirsrClass(1, 2)
y = FirsrClass(3, 4)

x.do_something()
y.do_something()

# print(x.a, y.a, x.class_attr, y.class_attr)