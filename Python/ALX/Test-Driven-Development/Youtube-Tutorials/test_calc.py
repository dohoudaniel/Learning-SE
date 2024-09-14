#!/usr/bin/python3
import unittest
import calc


class TestCalc(unittest.TestCase):
    def test_add(self):
        # The code below can replace the code two lines after it
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)
        # result = calc.add(10, 5)
        # self.assertEqual(result, 15)
        # No matter how many times that self.assertEqual is run,
        # it is shown as only one test during testing,
        # and this is because, it is just one assert method.

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)

        # Testing if an error is raised when division by zero occurs
        # self.assertRaises(ValueError, calc.divide, 7, 0)

        # Testing for exceptions using a context manager
        with self.assertRaises(ValueError):
            calc.divide(10, 0)
            # This line doesn't work - calc.divide(100, 2)


# Running a unittest directly on a file by compiling the file using python3
if __name__ == "__main__":
    unittest.main()
