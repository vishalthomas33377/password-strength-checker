import unittest
from password_checker import analyze_password

class PasswordCheckerTests(unittest.TestCase):
    def test_short_password_is_weak(self):
        self.assertEqual(analyze_password("abc")["rating"], "Weak")

    def test_common_password_is_weak(self):
        self.assertEqual(analyze_password("password123")["rating"], "Weak")

    def test_long_mixed_password_can_be_strong(self):
        self.assertEqual(analyze_password("Violet!River82#")["rating"], "Strong")

    def test_password_is_not_in_result(self):
        password = "MyTest!Pass123"
        self.assertNotIn(password, str(analyze_password(password)))

if __name__ == "__main__":
    unittest.main()
