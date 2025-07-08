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

def main():
    """主函数，展示计算器功能并与用户交互"""
    print("===== 简单计算器程序 =====")
    print("本程序提供加法和乘法计算功能")
    
    try:
        # 用户输入
        print("\n请输入两个数字进行计算:")
        num1 = float(input("请输入第一个数字: "))
        num2 = float(input("请输入第二个数字: "))
        
        # 显示计算结果
        print("\n计算结果:")
        print(f"{num1} + {num2} = {add(num1, num2)}")
        print(f"{num1} × {num2} = {multiply(num1, num2)}")
        
    except ValueError:
        print("\n错误: 请输入有效的数字!")
    except Exception as e:
        print(f"\n发生错误: {e}")
    
    # 防止程序闪退
    print("\n按回车键退出程序...")
    input()

if __name__ == "__main__":
    main() 