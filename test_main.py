import unittest
from main import add, subtract, multiply, divide

class TestMathFunctions(unittest.TestCase):
    
    def test_add(self):
        """测试加法函数"""
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)
    
    def test_subtract(self):
        """测试减法函数"""
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(5, 5), 0)
        self.assertEqual(subtract(-5, 5), -10)
    
    def test_multiply(self):
        """测试乘法函数"""
        self.assertEqual(multiply(6, 7), 42)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(-3, 4), -12)
    
    def test_divide(self):
        """测试除法函数"""
        self.assertEqual(divide(8, 2), 4)
        self.assertEqual(divide(5, 2), 2.5)
        self.assertEqual(divide(-6, 2), -3)
        
        # 测试除以零的异常
        with self.assertRaises(ValueError):
            divide(8, 0)

if __name__ == "__main__":
    unittest.main() 