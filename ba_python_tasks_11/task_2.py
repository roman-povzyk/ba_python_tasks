# Implement a class Mathematician which is a helper class for doing math operations on lists
# The class doesn't take any attributes and only has methods:

# square_nums(takes a list of integers and returns the list
# of squares) remove_positives(takes a list of integers and returns
# it without positive numbers filter_leaps(takes a list
# of dates(integers) and removes those that are not 'leap years'
# ```
# class Mathematician:
#     pass
# m = Mathematician()
# assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
# assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
# assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]

class Mathematician:

    def square_nums(self, list):
        a_list = []
        for i in list:
            a_list.append(i ** 2)
        return a_list

    def remove_positives(self, list):
        a_list = []
        for i in list:
            if not (i > 0):
                a_list.append(i)
        return a_list

    def filter_leaps(self, list):
        a_list = []
        for i in list:
            if i % 4 == 0:
                if i % 100 != 0 or i % 400 == 0:
                    a_list.append(i)
        return a_list


m = Mathematician()
print(m.square_nums([7, 11, 5, 4]))
print(m.remove_positives([26, -11, -8, 13, -90]))
print(m.filter_leaps([2001, 1884, 1995, 2003, 2020]))
