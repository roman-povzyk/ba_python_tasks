# Writing tests for context manager
#
# Take your implementation of the context manager class from Task 1
# and write tests for it. Try to cover as many use cases as you can,
# positive ones when a file exists and everything works as designed.
# And also, write tests when your class raises errors or you have
# errors in the runtime context suite.

import unittest
from main import MyOpenFile_RP as ContMNG

class test(unittest.TestCase):

    def test_counter(self):
        start = ContMNG.get_num_of_usage()
        with ContMNG() as f:
            f.open_file('sea.txt', 'r')
        finish = ContMNG.get_num_of_usage()
        self.assertEqual(finish, start + 1)

    def test_counter_of_type(self):
        start = ContMNG.get_num_of_usage_types('txt')
        with ContMNG() as f:
            f.open_file('sea.txt', 'r')
        finish = ContMNG.get_num_of_usage_types('txt')
        self.assertEqual(finish, start + 1)

    def test_counter_of_type_not_in_list(self):
        start = ContMNG.get_num_of_usage_types('test44')
        with ContMNG() as f:
            f.open_file('sea.txt', 'r')
        finish = ContMNG.get_num_of_usage_types('test44')
        self.assertEqual(finish, start + 1)

    def test_file_types(self):
        start = ContMNG.file_types['other']
        try:
            with ContMNG() as f:
                f.open_file('1.test')
        except TypeError as error:
            self.assertEqual(str(error), 'Тип файлу недоступний.')
        finish = ContMNG.file_types['other']
        self.assertEqual(finish, start + 1)

    def test_open_file(self):
        with ContMNG() as f:
            x = f.open_file('sea.txt')
            status_file = x.closed
        self.assertEqual(status_file, True)
