import unittest
from lab10 import LibraryItem

class TestLibraryItem(unittest.TestCase):

    def test_details_standard(self):
        item = LibraryItem("Kobzar", "Taras Shevchenko", 1840)
        expected = "Title: Kobzar, Author: Taras Shevchenko, Year: 1840"
        self.assertEqual(item.details(), expected)

    def test_details_with_special_chars(self):
        item = LibraryItem("1984", "George Orwell", 1949)
        expected = "Title: 1984, Author: George Orwell, Year: 1949"
        self.assertEqual(item.details(), expected)

    def test_details_modern_year(self):
        item = LibraryItem("Python Deep Learning", "Ivan Ivanov", 2023)
        expected = "Title: Python Deep Learning, Author: Ivan Ivanov, Year: 2023"
        self.assertEqual(item.details(), expected)


if __name__ == '__main__':
    unittest.main()
