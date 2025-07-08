#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
测试模块
用于测试main.py中的数学运算函数
"""

import unittest
from main import add, subtract, multiply, divide


class TestMathFunctions(unittest.TestCase):
    """测试数学运算函数的测试类"""
    
    def test_add(self):
        """测试加法函数"""
        # 基本测试
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)
        
        # 边界测试
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(999999, 1), 1000000)
        
        # 浮点数测试
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=10)
    
    def test_subtract(self):
        """测试减法函数"""
        # 基本测试
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(5, 5), 0)
        self.assertEqual(subtract(-5, 5), -10)
        
        # 边界测试
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(1000000, 1), 999999)
        
        # 浮点数测试
        self.assertAlmostEqual(subtract(0.3, 0.1), 0.2, places=10)
    
    def test_multiply(self):
        """测试乘法函数"""
        # 基本测试
        self.assertEqual(multiply(6, 7), 42)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(-3, 4), -12)
        self.assertEqual(multiply(-3, -4), 12)
        
        # 边界测试
        self.assertEqual(multiply(0, 0), 0)
        self.assertEqual(multiply(1, 999999), 999999)
        
        # 浮点数测试
        self.assertAlmostEqual(multiply(0.1, 0.1), 0.01, places=10)
    
    def test_divide(self):
        """测试除法函数"""
        # 基本测试
        self.assertEqual(divide(8, 2), 4)
        self.assertEqual(divide(5, 2), 2.5)
        self.assertEqual(divide(-6, 2), -3)
        self.assertEqual(divide(-6, -2), 3)
        
        # 边界测试
        self.assertEqual(divide(0, 5), 0)
        self.assertAlmostEqual(divide(1, 3), 0.3333333333, places=5)
        
        # 测试除以零的异常
        with self.assertRaises(ValueError):
            divide(8, 0)
        with self.assertRaises(ValueError):
            divide(0, 0)


if __name__ == "__main__":
    unittest.main() 