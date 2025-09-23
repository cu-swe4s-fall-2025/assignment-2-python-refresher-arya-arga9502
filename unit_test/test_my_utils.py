import my_utils
import unittest
import numpy as np

class CalcTest(unittest.TestCase):
    def test_mean(self):
        numbers = np.random.randint(1, 101, size=10)
        mean = np.mean(numbers)
        sd = np.std(numbers)
        num = [1,2,3,4,5]
        self.assertEqual(my_utils.get_mean(numbers),mean)
        self.assertEqual(my_utils.get_mean(num),3)
        self.assertNotEqual(my_utils.get_mean(numbers),sd)
        self.assertNotEqual(my_utils.get_mean(numbers),102)


    def test_median(self):
        numbers = np.random.randint(1, 101, size=10)
        median = np.median(numbers)
        sd = np.std(numbers)
        num = [2,5,6,9,300]
        self.assertEqual(my_utils.get_median(numbers),median)
        self.assertEqual(my_utils.get_median(num),6)
        self.assertNotEqual(my_utils.get_median(numbers),sd)
        self.assertNotEqual(my_utils.get_median(numbers),102)


    def test_sd(self):
        numbers = np.random.randint(1, 101, size=10)
        sd = np.std(numbers)
        median = np.median(numbers)
        num = [4,6,10,33,21]
        self.assertEqual(my_utils.get_sd(numbers),sd)
        self.assertAlmostEqual(my_utils.get_sd(num),10.83,places=2)
        self.assertNotEqual(my_utils.get_sd(numbers),102)
        self.assertNotEqual(my_utils.get_sd(numbers),median)

if __name__ == "__main__":
    unittest.main()


