# PYtest

一个简单的Python计算器程序，可以进行基本的数学运算。

## 项目简介

本项目实现了一个简单的计算器程序，包含加法和乘法两种基本数学运算功能，并提供了用户交互界面。

## 项目结构

```
PYtest/
├── main.py                  # 主模块，包含数学运算函数和用户交互
├── test_main.py             # 测试模块，包含单元测试
└── README.md                # 项目说明文档
```

## 功能特性

本项目实现了以下数学运算函数：

- **加法 (add)**: 计算两个数的和
- **乘法 (multiply)**: 计算两个数的积

## 使用方法

### 直接运行

```bash
python main.py
```

### 创建可执行文件

可以使用PyInstaller将Python脚本打包成可执行文件：

1. 首先安装PyInstaller：

```bash
pip install pyinstaller
```

2. 创建可执行文件：

```bash
# 创建单文件可执行程序
pyinstaller --onefile main.py

# 或创建带窗口的可执行程序（推荐，不会显示控制台窗口）
pyinstaller --onefile --noconsole main.py
```

3. 生成的可执行文件将位于`dist`目录中

### 运行测试

使用Python的unittest框架运行测试：

```bash
python -m unittest discover
```

或者直接运行测试文件：

```bash
python test_main.py
```

## 常见问题解决

如果可执行文件运行后立即闪退，可能是因为：

1. 程序执行完毕后自动关闭 - 已通过在程序末尾添加`input()`语句解决
2. 程序出现错误 - 已添加异常处理来显示错误信息

## 注意事项

- 本程序使用Python 3编写
- 创建可执行文件需要PyInstaller库
- 程序会在结束时等待用户按回车键，防止窗口立即关闭
