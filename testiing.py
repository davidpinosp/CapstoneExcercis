import unittest
from main import order

a = order("asc")

class TestOrder(unittest.TestCase):
    def test_order(self):
        self.assertEqual(a[0], 1)



if __name__ == '__main__':
    unittest.main()