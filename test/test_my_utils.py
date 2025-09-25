import unittest
import numpy as np
import sys

sys.path.append("src")  # noqa

import my_utils


class CalcTest(unittest.TestCase):
    def test_mean(self):  # test the mean function defined in my_utils
        for i in range(1000):
            # randomly generate 10 numbers between 1 and 100
            numbers = np.random.randint(1, 100, size=10)
            mean = np.mean(numbers)  # find mean using the np library
            self.assertEqual(my_utils.get_mean(numbers), mean)
            self.assertNotEqual(my_utils.get_mean(numbers), 102)
            self.assertTrue(1 <= mean <= 100)
        list1 = [1, 2, 3, 4, 5]
        self.assertEqual(my_utils.get_mean(list1), 3)
        list2 = [-1, -2, -3, -4, -5]
        self.assertEqual(my_utils.get_mean(list2), -3)


def test_median(self):  # test the median function defined in my_utils
    for i in range(1000):
        # randomly generate 10 numbers between 1 and 100
        numbers = np.random.randint(1, 100, size=10)
        median = np.median(numbers)  # find median using the np library
        self.assertEqual(my_utils.get_median(numbers), median)
        self.assertNotEqual(my_utils.get_median(numbers), 102)
        self.assertTrue(1 <= median <= 100)
    list1 = [2, 3, 70, 90, 1000]
    self.assertEqual(my_utils.get_median(list1), 70)
    list2 = [-12, -30, -7, -9, -1000]
    self.assertEqual(my_utils.get_median(list2), -12)


def test_sd(self):  # test the standard deviation function defined in my_utils
    for i in range(1000):
        # randomly generate 10 numbers between 1 and 100
        numbers = np.random.randint(1, 100, size=10)
        sd = np.std(numbers)  # find sd using the np library
        self.assertAlmostEqual(my_utils.get_sd(numbers), sd, places=2)
        self.assertNotEqual(my_utils.get_sd(numbers), 102)
        self.assertTrue(1 <= sd <= 100)
    list1 = [4, 6, 10, 33, 21]
    self.assertAlmostEqual(my_utils.get_sd(list1), 10.83, places=2)
    list2 = [-1, -2, -3, -4, -5]
    self.assertAlmostEqual(my_utils.get_sd(list2), 1.41, places=2)


if __name__ == "__main__":
    unittest.main()
