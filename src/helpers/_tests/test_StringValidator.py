import unittest
from StringValidator import StringValidator


class TestStringValidator(unittest.TestCase):

    def setUp(self):
        self.validator = StringValidator()

    def test_is_valid_string(self):
        # Test valid string
        valid_str = "This is a valid string"
        self.assertTrue(self.validator.is_valid_string(valid_str))

        # Test invalid string - contains numbers
        invalid_str = "Invalid string 123"
        self.assertFalse(self.validator.is_valid_string(invalid_str))

        # Test invalid string - contains special characters
        invalid_str = "Invalid string *&^%"
        self.assertFalse(self.validator.is_valid_string(invalid_str))

        # Test invalid string - empty string
        invalid_str = ""
        self.assertFalse(self.validator.is_valid_string(invalid_str))

        # Test invalid string - None
        invalid_str = None
        self.assertFalse(self.validator.is_valid_string(invalid_str))

    def test_is_valid_email(self):
        # Test valid email
        valid_email = "test@example.com"
        self.assertTrue(self.validator.is_valid_email(valid_email))

        # Test invalid email - missing @
        invalid_email = "testexample.com"
        self.assertFalse(self.validator.is_valid_email(invalid_email))

        # Test invalid email - missing domain
        invalid_email = "test@"
        self.assertFalse(self.validator.is_valid_email(invalid_email))

        # Test invalid email - missing username
        invalid_email = "@example.com"
        self.assertFalse(self.validator.is_valid_email(invalid_email))

        # Test invalid email - empty string
        invalid_email = ""
        self.assertFalse(self.validator.is_valid_email(invalid_email))

        # Test invalid email - None
        invalid_email = None
        self.assertFalse(self.validator.is_valid_email(invalid_email))


if __name__ == '__main__':
    unittest.main()
