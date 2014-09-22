import unittest
from fizz_buzz import FizzBuzz

class FizzBuzzTest(unittest.TestCase):
    def test_number(self):
        self.number(FizzBuzz(1),1)

if __name__ == '__main__':
    unittest.main()
