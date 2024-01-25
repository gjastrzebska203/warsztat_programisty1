import unittest
from main import sum

class TestMojProgram(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(2, 4), 6)
        self.assertEqual(sum(-10, 10), 0)
        self.assertEqual(sum(1, 5), 6)

if __name__ == '__main__':
    unittest.main()
