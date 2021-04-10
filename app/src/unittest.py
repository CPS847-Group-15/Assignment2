import unittest
from app.src.fizzbuzz import fb

class TestFizzBuzz(unittest.TestCase):
    def test_fizz(self):
        self.assertEqual(fb(3), "fizz", "Should return 'fizz'")
        self.assertEqual(fb(12), "fizz", "Should return 'fizz'")
        self.assertEqual(fb(18), "fizz", "Should return 'fizz'")
        self.assertEqual(fb(306), "fizz", "Should return 'fizz'")
        self.assertEqual(fb(903), "fizz", "Should return 'fizz'")

    def test_buzz(self):
        self.assertEqual(fb(5), "buzz", "Should return 'buzz'")
        self.assertEqual(fb(20), "buzz", "Should return 'buzz'")
        self.assertEqual(fb(25), "buzz", "Should return 'buzz'")
        self.assertEqual(fb(10), "buzz", "Should return 'buzz'")
        self.assertEqual(fb(35), "buzz", "Should return 'buzz'")
        self.assertEqual(fb(10010), "buzz", "Should return 'buzz'")

    def test_fizz_buzz(self):
        self.assertEqual(fb(15), "fizz buzz", "Should return 'fizz buzz'")
        self.assertEqual(fb(30), "fizz buzz", "Should return 'fizz buzz'")
        self.assertEqual(fb(45), "fizz buzz", "Should return 'fizz buzz'")
        self.assertEqual(fb(105), "fizz buzz", "Should return 'fizz buzz'")
        self.assertEqual(fb(120), "fizz buzz", "Should return 'fizz buzz'")

    def test_zero(self):
        self.assertEqual(fb(0), "0", "Should return '0'")

    def test_numbers(self):
        self.assertEqual(fb(1), "1", "Should return '1'")
        self.assertEqual(fb(2), "2", "Should return '2'")
        self.assertEqual(fb(4), "4", "Should return '4'")
        self.assertEqual(fb(22), "22", "Should return '22'")
        self.assertEqual(fb(16), "16", "Should return '16'")
        self.assertEqual(fb(64), "64", "Should return '64'")
        self.assertEqual(fb(164), "164", "Should return '164'")