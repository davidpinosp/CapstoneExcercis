import unittest
from main import order

a = order("asc")
b = order("desc")

class TestOrder(unittest.TestCase):
    def test_order(self):
        self.assertEqual(a[0], 1)
        self.assertEqual(b[0], 7678)


if __name__ == '__main__':
    unittest.main()