def add(a, b):
    """将两个数相加并返回结果"""
    return a + b

def subtract(a, b):
    """将两个数相减并返回结果"""
    return a - b

def multiply(a, b):
    """将两个数相乘并返回结果"""
    return a * b

def divide(a, b):
    """将两个数相除并返回结果"""
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b

if __name__ == "__main__":
    print("简单计算器程序")
    print("5 + 3 =", add(5, 3))
    print("10 - 4 =", subtract(10, 4))
    print("6 * 7 =", multiply(6, 7))
    print("8 / 2 =", divide(8, 2)) 