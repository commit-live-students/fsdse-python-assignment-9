from unittest import TestCase
from errors import incorrect_output, no_function_found, succeed
import ast
from pprint import pprint

class TestValidate_email(TestCase):
    def test_validate_email(self):
        try:
            from email import validate_email
        except ImportError:
            self.assertFalse(no_function_found("validate_email"))

        check = False

        s = "sangam@greyatom.com"

        solution = validate_email(s)


        self.assertNotEqual(None, solution)

        self.assertEqual(True, solution)