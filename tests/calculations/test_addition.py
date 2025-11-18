import unittest

from app.calculations.addition import add_numbers


class TestAddNumbers(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)

    def test_negative_numbers(self):
        self.assertEqual(add_numbers(-2, -3), -5)

    def test_mixed_sign_numbers(self):
        self.assertEqual(add_numbers(-2, 5), 3)

    def test_zero(self):
        self.assertEqual(add_numbers(0, 7), 7)
        self.assertEqual(add_numbers(7, 0), 7)


if __name__ == '__main__':
    unittest.main()
