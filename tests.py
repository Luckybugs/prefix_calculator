import unittest

from calculator import prefix_eval

class TestPrefexEval(unittest.TestCase):
    def test_1(self):
        input =' + 3 4 '
        result = prefix_eval(input)
        self.assertEqual(result, 7)
    
    def test_2(self):
        input ='- 9 4'
        result = prefix_eval(input)
        self.assertEqual(result, 5)

    def test_3(self):
        input ='/ * 309 3 * + 23 9 - 8 3'
        result = prefix_eval(input)
        self.assertEqual(result, 5.79375)
    
    def test_4(self):
        input = '- 12 * 2 6'
        result = prefix_eval(input)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
