# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：

# -*- coding: utf-8 -*-
from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def fn(x,y):
    return x*10+y

def char2num(s):
    return DIGITS[s]

def str2float(s):
    return reduce(fn,map(char2num,s.split('.')[0]))+reduce(fn,map(char2num,s.split('.')[1]))/10**len(s.split('.')[1])

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')