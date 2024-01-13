import unittest
from StringNormalizer import StringNormalizer


class TestStringNormalizer(unittest.TestCase):

    def setUp(self):
        self.normalizer = StringNormalizer()

    def test_normalize_string_with_lowercase(self):
        # Test that a string with only lowercase letters is returned unchanged
        input_str = 'this is a lowercase string'
        expected_output = 'this is a lowercase string'
        self.assertEqual(self.normalizer.normalize_string(
            input_str), expected_output)

    def test_normalize_string_with_uppercase(self):
        # Test that a string with only uppercase letters is converted to lowercase
        input_str = 'THIS IS AN UPPERCASE STRING'
        expected_output = 'this is an uppercase string'
        self.assertEqual(self.normalizer.normalize_string(
            input_str), expected_output)

    def test_normalize_string_with_mixed_case(self):
        # Test that a string with mixed case is converted to lowercase
        input_str = 'This Is A MIXED CASE String'
        expected_output = 'this is a mixed case string'
        self.assertEqual(self.normalizer.normalize_string(
            input_str), expected_output)

    def test_normalize_string_with_punctuation(self):
        # Test that punctuation is removed from the string
        input_str = 'This string has a comma, a period. and a colon:'
        expected_output = 'this string has a comma a period and a colon'
        self.assertEqual(self.normalizer.normalize_string(
            input_str), expected_output)

    def test_normalize_string_with_numbers(self):
        # Test that numbers are removed from the string
        input_str = 'This string has 123 numbers in it'
        expected_output = 'this string has   numbers in it'
        self.assertEqual(self.normalizer.normalize_string(
            input_str), expected_output)

    def test_normalize_string_with_whitespace(self):
        # Test that excess whitespace is removed from the string
        input_str = '   This string has   extra    whitespace   '
        expected_output = 'this string has extra whitespace'
        self.assertEqual(self.normalizer.normalize_string(
            input_str), expected_output)


if __name__ == '__main__':
    unittest.main()
