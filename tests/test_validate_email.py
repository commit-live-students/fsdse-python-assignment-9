from unittest import TestCase
from errors import incorrect_output, no_function_found, succeed
import ast
from pprint import pprint

class TestValidate_email(TestCase):
    def test_validate_email(self):
        try:
            from build import validate_email
        except ImportError:
            self.assertFalse(no_function_found("validate_email"))

        check = False
        tree = ast.parse(''.join(open("../email.py")))
        for node in tree.body:
            if isinstance(node, ast.FunctionDef):
                if node.name == "validate_email":
                    for nodelist in node.body:
                        if hasattr(nodelist, 'targets'):
                            i = 0
                            for target in nodelist.targets:
                                if target.id == "pattern":
                                    self.assertEqual("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", nodelist.value.args[i].s)
                                    check = True
                                    break
                                i = i + 1
        if check:
            self.assertTrue(succeed("test cases are passed"))
        else:
            self.assertFalse(no_function_found("pattern keyword"))
