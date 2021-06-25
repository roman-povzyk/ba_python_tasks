# Create your own implementation of an iterable,
# which could be used inside for-in loop.
# Also, add logic for retrieving elements using square brackets syntax.

class CountSevenDiv:
    """My own implementation of an iterable."""

    def __init__(self, start=0):
        self.num = start
        self.list = []

    def __iter__(self):
        return self

    def __next__(self):
        self.num += 7
        self.list.append(self.num)
        return self.list


seven_div = CountSevenDiv()
seven_div_iter = iter(seven_div)

# створюю список елементів від 7 до 700, кратний 7 + виводжу його останнє число за індексом -1
for i in range(100):
    current_list = next(seven_div_iter)
    print(f'Останній елемент наразі — {current_list[-1]}, весь список — {current_list}')
