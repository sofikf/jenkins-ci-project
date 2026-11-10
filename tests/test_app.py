
import unittest
from app import add_numbers, subtract_numbers, multiply_numbers


class TestApplication(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(add_numbers(2, 3), 5)

    def test_subtraction(self):
        self.assertEqual(subtract_numbers(5, 2), 3)

    def test_multiplication(self):
        self.assertEqual(multiply_numbers(4, 3), 12)


if __name__ == "__main__":
    unittest.main()
