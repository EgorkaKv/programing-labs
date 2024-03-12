import unittest
from src import lab2


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(lab2.buying([[1,2],[2,2],[3,1]],7,3), 2)

    def test_2(self):
        self.assertEqual(lab2.buying([[5,0],[2,2],[1,4],[5,1]],19,4),3)

    def test_3(self):
        self.assertEqual(lab2.buying([[1,5000],[1,6000]],2,2),1)


if __name__ == '__main__':
    unittest.main()
