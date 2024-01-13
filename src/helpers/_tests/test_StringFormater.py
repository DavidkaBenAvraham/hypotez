import unittest
from StringFormatter import StringFormatter


class TestStringFormatter(unittest.TestCase):

    def test_remove_special_characters(self):
        formatter = StringFormatter()
        self.assertEqual(formatter.remove_special_characters(
            "Hello World!"), "Hello World")
        self.assertEqual(formatter.remove_special_characters(
            "I'm excited for summer!"), "Im excited for summer")

    def test_capitalize_first_letter(self):
        formatter = StringFormatter()
        self.assertEqual(formatter.capitalize_first_letter(
            "hello world"), "Hello world")
        self.assertEqual(formatter.capitalize_first_letter(
            "what's up?"), "What's up?")

    def test_reverse_string(self):
        formatter = StringFormatter()
        self.assertEqual(formatter.reverse_string(
            "hello world"), "dlrow olleh")
        self.assertEqual(formatter.reverse_string("what's up?"), "?pu s'tahw")

    def test_format_string(self):
        formatter = StringFormatter()
        self.assertEqual(formatter.format_string(
            "Hello, {0}! Today is {1}.", "Alice", "Monday"), "Hello, Alice! Today is Monday.")
        self.assertEqual(formatter.format_string(
            "{0} is {1} years old.", "Bob", 25), "Bob is 25 years old.")
