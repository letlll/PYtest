# PYtest

[![Python Tests](https://github.com/username/PYtest/actions/workflows/python-test.yml/badge.svg)](https://github.com/username/PYtest/actions/workflows/python-test.yml)

一个用于GitHub Actions自动化测试学习的简单Python项目。

## 项目简介

本项目实现了一个简单的计算器库，包含基本的数学运算功能，并通过GitHub Actions实现了自动化测试流程。

## 项目结构

```
PYtest/
├── .github/
│   └── workflows/
│       └── python-test.yml  # GitHub Actions工作流配置
├── main.py                  # 主模块，包含数学运算函数
├── test_main.py             # 测试模块，包含单元测试
└── README.md                # 项目说明文档
```

## 功能特性

本项目实现了以下数学运算函数：

- **加法 (add)**: 计算两个数的和
- **减法 (subtract)**: 计算两个数的差
- **乘法 (multiply)**: 计算两个数的积
- **除法 (divide)**: 计算两个数的商，并处理除零异常

## 使用方法

### 安装依赖

本项目不需要额外的依赖，只使用Python标准库。

### 运行主程序

```bash
python main.py
```

### 运行测试

使用Python的unittest框架运行测试：

```bash
python -m unittest discover
```

或者直接运行测试文件：

```bash
python test_main.py
```

## GitHub Actions自动化测试

本项目配置了GitHub Actions工作流，当代码推送到main或master分支，或者创建针对这些分支的Pull Request时，会自动运行测试。

工作流程配置文件位于 `.github/workflows/python-test.yml`，主要步骤包括：

1. 检出代码
2. 设置Python环境
3. 安装依赖（如有）
4. 运行单元测试

## 贡献指南

欢迎提交Issue和Pull Request来改进本项目。

## 许可证

MIT
