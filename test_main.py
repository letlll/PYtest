#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
测试模块
用于测试main.py中的数学运算函数
"""

import unittest
from main import add, multiply


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


if __name__ == "__main__":
    unittest.main() 