# Pick your solution to one of the exercises in this module.
# Design tests for this solution and write tests using unittest library.


import unittest
import ba_python_tasks_13.task_3


class NameTestCase(unittest.TestCase):

    def test_choose_func(self):
        choose_func_example_1 = ba_python_tasks_13.task_3.choose_func([1, 2, 3, 4, 5],
                                                                      ba_python_tasks_13.task_3.square_nums,
                                                                      ba_python_tasks_13.task_3.remove_negatives)
        choose_func_example_2 = ba_python_tasks_13.task_3.choose_func([1, -2, 3, -4, 5],
                                                                      ba_python_tasks_13.task_3.square_nums,
                                                                      ba_python_tasks_13.task_3.remove_negatives)
        self.assertEqual(choose_func_example_1, [1, 4, 9, 16, 25])
        self.assertEqual(choose_func_example_2, [1, 3, 5])
        self.assertNotEqual(choose_func_example_1, [1, 4, 9, 17, 25])
        self.assertNotEqual(choose_func_example_2, [1, 3, 6])


unittest.main()
