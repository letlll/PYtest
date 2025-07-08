#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
简单计算器模块
提供基本的数学运算功能
"""

def add(a, b):
    """
    将两个数相加并返回结果
    
    参数:
        a: 第一个数
        b: 第二个数
    
    返回:
        两数之和
    """
    return a + b

def subtract(a, b):
    """
    将两个数相减并返回结果
    
    参数:
        a: 被减数
        b: 减数
    
    返回:
        两数之差
    """
    return a - b

def multiply(a, b):
    """
    将两个数相乘并返回结果
    
    参数:
        a: 第一个因数
        b: 第二个因数
    
    返回:
        两数之积
    """
    return a * b

def divide(a, b):
    """
    将两个数相除并返回结果
    
    参数:
        a: 被除数
        b: 除数
    
    返回:
        两数之商
        
    异常:
        ValueError: 当除数为零时抛出
    """
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b


def main():
    """主函数，展示计算器功能"""
    print("===== 简单计算器程序 =====")
    print("加法示例: 5 + 3 =", add(5, 3))
    print("减法示例: 10 - 4 =", subtract(10, 4))
    print("乘法示例: 6 * 7 =", multiply(6, 7))
    print("除法示例: 8 / 2 =", divide(8, 2))
    
    try:
        print("错误示例: 8 / 0 =", divide(8, 0))
    except ValueError as e:
        print(f"错误: {e}")


if __name__ == "__main__":
    main() 