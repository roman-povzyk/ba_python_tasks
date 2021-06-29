import unittest
import task_1_example_for_test


class NameTestCase(unittest.TestCase):

    def test_choose_func(self):
        choose_func_example_1 = task_1_example_for_test.choose_func([1, 2, 3, 4, 5],
                                                                    task_1_example_for_test.square_nums,
                                                                    task_1_example_for_test.remove_negatives)
        choose_func_example_2 = task_1_example_for_test.choose_func([1, -2, 3, -4, 5],
                                                                    task_1_example_for_test.square_nums,
                                                                    task_1_example_for_test.remove_negatives)
        self.assertEqual(choose_func_example_1, [1, 4, 9, 16, 25])
        self.assertEqual(choose_func_example_2, [1, 3, 5])
        self.assertNotEqual(choose_func_example_1, [1, 4, 9, 17, 25])
        self.assertNotEqual(choose_func_example_2, [1, 3, 6])


unittest.main()
