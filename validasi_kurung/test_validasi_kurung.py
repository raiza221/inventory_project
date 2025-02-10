import unittest
from validasi_kurung import is_valid_parentheses

class TestValidParentheses(unittest.TestCase):
    def test_cases(self):
        self.assertTrue(is_valid_parentheses("{[()]}"))
        self.assertFalse(is_valid_parentheses("{[(])}"))
        self.assertTrue(is_valid_parentheses("()[]{}"))
        self.assertFalse(is_valid_parentheses("([)]"))
        self.assertTrue(is_valid_parentheses(""))
        self.assertFalse(is_valid_parentheses("{{{{"))

if __name__ == "__main__":
    unittest.main()
