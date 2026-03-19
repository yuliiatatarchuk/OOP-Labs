import unittest
from lab10 import check_even
from parameterized import parameterized
class TestCheckEven(unittest.TestCase):
    @parameterized.expand([
        ("even", 4, True),
        ("odd", 5, False),
        ("zero", 0, True),
        ("negative_even", -2, True),])
    def test_even_logic(self, name, val, expected):
        self.assertEqual(check_even(val), expected)


if __name__ == '__main__':
    unittest.main()