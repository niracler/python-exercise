# python-exercise

> 关于python的面试题及leetcode题目代码实现

## 目录

## Python基础

### 文件操作

1. [写一个返回该文件夹中文件的路径,以及其包含文件夹中文件的路径的函数](interview_question/print_dir.py)

### 模块与包

1. [函数输入为年月日，输出这是该年的第几天](interview_question/get_date.py)

1. [打乱一个排好序的list对象alist？](interview_question/upset_a_list.py)

### 数据类型

1. [现有字典 d= {'a':24,'g':52,'i':12,'k':33}请按value值进行排序?](interview_question/sort_dicts.py)

1. [请反转字符串 "aStr"?](interview_question/reverse_str.py)

1. [将字符串 "k:1 |k1:2|k2:3|k3:4"，处理成字典 {k:1,k1:2,...}](interview_question/to_dicts.py)

1. [请按alist中元素的age由大到小排序](interview_question/sort_list.py)

1. 下面代码的输出结果将是什么？

```python
list = ['a','b','c','d','e']
print(list[10:])
```

代码将会输出[]， 不会产生IndexError错误， 就像所期望的那样，尝试用超出成员的个数的index来获取某个列表的成员。例如尝试获取list[10]和之后的成员，会导致IndexError。然而， 尝试获取列表的切片，开始的index超过了成员个数不会产生IndexError， 而是仅仅返回一个空列表。这成为特别让人恶心的疑难杂症， 因为运行的时候没有产生错误，导致BUG很难被追踪到。

1. [写一个列表生成式，产生一个公差为11的等差数列](interview_question/gen_list.py)


### LeetCode热门面试问题

1. [两个数相加的和等于某个数](leetcode/two_sum.py)

## 参考文章

- [关于python的面试题](https://github.com/Niracler/python-interview-question)  
- [python-exercises](https://www.w3resource.com/python-exercises/)
