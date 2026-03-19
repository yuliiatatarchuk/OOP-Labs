import unittest
from lab10 import MathTool
class TestMathTool(unittest.TestCase):
    def setUp(self):
        self.tool = MathTool()

    def test_add(self):
        self.assertEqual(self.tool.add(10, 5), 15)
        self.assertEqual(self.tool.add(-1, 1), 0)

    def test_sub(self):
        self.assertEqual(self.tool.sub(10, 5), 5)
        self.assertEqual(self.tool.sub(0, 5), -5)

    def test_mul(self):
        self.assertEqual(self.tool.mul(10, 5), 50)
        self.assertEqual(self.tool.mul(10, 0), 0)

    def test_div(self):
        self.assertEqual(self.tool.div(10, 2), 5.0)
        self.assertEqual(self.tool.div(10, 4), 2.5)

    def test_div_by_zero(self):
        with self.assertRaises(ValueError):
            self.tool.div(10, 0)

if __name__ == "__main__":
    unittest.main()
