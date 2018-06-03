import unittest
import calc

class TestCalc(unittest.TestCase):
    
    def test_add(self):
        result = calc.add(10, 5)
        self.assertEqual(result, 15)

    def test_sub(self):
        result = calc.sub(1, 1)
        self.assertEqual(result, 0)

    def test_multiply(self):
        result = calc.multiply(2, 2)
        self.assertEqual(result, 4)

    def test_divide(self):
        result = calc.divide(2, 2)
        self.assertEqual(result, 1)
        
    def test_raise_when_dividing_by_zero(self):
        # self.assertRaises(ValueError, calc.divide, 1, 0)
        with self.assertRaises(ValueError):
            calc.divide(10, 0)

if __name__ == '__main__':
    unittest.main()