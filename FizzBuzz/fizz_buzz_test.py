import unittest
from fizz_buzz import fizz_buzz

class FizzBuzzTest(unittest.TestCase):
    def test_fizz_buzz_one(self):
        self.assertEqual(fizz_buzz(1),1)

    def test_fizz_buzz_two(self):
        self.assertEqual(fizz_buzz(2), 2)

    def test_fizz_buzz_four(self):
        self.assertEqual(fizz_buzz(4), 4)


if __name__ == '__main__':
    unittest.main()
