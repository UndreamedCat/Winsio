# Winsio
## 关于此项目
**Winsio** 是一个让你可以在 Windows/Linux 上运行和 Casio 计算器类似的内容的项目。  
## 此项目预计会支持的：
+ 美观的界面（基于 `PyQt6-Fluent-Widgets` 库）
+ 正常计算器
+ 解方程，包括一元一次，一元二次和二元一次方程（组）
+ 函数绘图（基于 `matplotlib`）
+ 求二次函数的极值点（可能使用顶点式或三分算法）
+ 自定义的 Python 程序
+ 允许你通过 AI API 让 AI 给你解题！

## 此项目目前支持的：
+ 一个不太美观的界面。
+ 暂时不支持正常计算器。

## 关于自定义程序
> 目前此类别暂未实现。
### 第一种方法
首先，程序接收您的一个输入 `user_module_name`，此输入为您将导入的自定义程序的文件名。
你的程序必须包含且仅包含一个函数 `Solver()`，且该函数应该接收一个字符串。  
同时，您的函数应该返回一个可以作为字符串输出的答案。  
Winsio 会接受用户输入的参数字符串 `param`，并如此调用您的函数：
```python
from importlib import import_module
user_module_name = ""       # 实际运行时从页面读取
param = "" 
user_module = import_module(user_module_name)
ans = user_module.Solver(param)
```
返回的 `ans` 将被置于输出框中。