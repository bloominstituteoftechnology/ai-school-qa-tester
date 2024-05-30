import unittest
import pytest
from app.string_reversal import reverse_string_exclude_special
from app.factorial import factorial
from app.fibonacci import fibonacci

class TestReverseStringExcludeSpecial(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(reverse_string_exclude_special('abc123'), '321cba', "Failed on typical case with alphanumeric characters")

    def test_with_special_characters(self):
        self.assertEqual(reverse_string_exclude_special('a!b@c#1$2%3^'), '3!2@1#c$b%a^', "Failed on case with special characters")

    def test_empty_string(self):
        self.assertEqual(reverse_string_exclude_special(''), '', "Failed on empty string")

    def test_only_special_characters(self):
        self.assertEqual(reverse_string_exclude_special('!@#$%^&*()'), '!@#$%^&*()', "Failed on string with only special characters")

    def test_palindrome(self):
        self.assertEqual(reverse_string_exclude_special('madam'), 'madam', "Failed on palindrome string")

    def test_mixed_case(self):
        self.assertEqual(reverse_string_exclude_special('AbC123'), '321CbA', "Failed on mixed case string")

    def test_numbers_only(self):
        self.assertEqual(reverse_string_exclude_special('123456'), '654321', "Failed on numbers only string")

    def test_single_character(self):
        self.assertEqual(reverse_string_exclude_special('a'), 'a', "Failed on single character string")

    def test_single_special_character(self):
        self.assertEqual(reverse_string_exclude_special('!'), '!', "Failed on single special character string")

class TestFactorial(unittest.TestCase):

    def test_factorial_positive_integer(self):
        self.assertEqual(factorial(5), 120)

    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_negative_integer(self):
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_factorial_one(self):
        self.assertEqual(factorial(1), 1)

    def test_factorial_large_number(self):
        self.assertEqual(factorial(10), 3628800)

class TestFibonacci(unittest.TestCase):

    def test_fibonacci_typical_cases(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(10), 55)

    def test_fibonacci_edge_cases(self):
        self.assertEqual(fibonacci(20), 6765)
        self.assertEqual(fibonacci(30), 832040)

    def test_fibonacci_invalid_input(self):
        with self.assertRaises(ValueError):
            fibonacci(-1)

if __name__ == '__main__':
    unittest.main()
