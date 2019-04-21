# """
# 题目：手写一个判断时间的装饰器
#
# """

import datetime

class TimeException(Exception):
    """
    关于时间异常的类
    """
    def __init__(self, execption_info):
        super().__init__()
        self.info = execption_info
    def __str__(self):
        return self.info

def timecheck(func):
    """
    检查今年是否是2019的装饰器
    """
    def wrapper(*args, **kwargs):
        if datetime.datetime.now().year == 2018:
            func(*args, **kwargs)
        else:
            raise TimeException("函数已过时")
    
    return wrapper

@timecheck
def test(name):
    print("Hello {}, 2018 Happy".format(name))

if __name__ == '__main__':
    test("niracler")

# """
# 分析:
#
# """
