import unittest
from fizz_buzz import fizz_buzz

class FizzBuzzTest(unittest.TestCase):
    def test_fizz_buzz_one(self):
        self.assertEqual(fizz_buzz(1),1)

    def test_fizz_buzz_two(self):
        self.assertEqual(fizz_buzz(2), 2)

    def test_fizz_buzz_four(self):
        self.assertEqual(fizz_buzz(4), 4)

    def test_multiple_three(self):
        self.assertEqual(fizz_buzz(3), "fizz")

    def test_multiple_five(self):
        self.assertEqual(fizz_buzz(5), "buzz")

    def test_multiple_three_and_five(self):
        self.assertEqual(fizz_buzz(15), "fizzbuzz")

if __name__ == '__main__':
    unittest.main()
