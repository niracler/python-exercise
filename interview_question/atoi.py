# """
# 题目：字符串 "123" 转换成 123，不使用内置api，例如 int()
#
# """
from functools import reduce


class Solution:
    def atoi1(self, a):
        """
        使用str(),与相应数字的string类型作比较
        :param a:
        :return:
        """
        num = 0
        for i in a:  # 循环每一个字符
            for j in range(10):
                if i == str(j):
                    num = num * 10 + j

        return num

    def atoi2(self, a):
        """
        使用ord函数,与“0”作比较
        :param a:
        :return:
        """
        num = 0
        for i in a:  # 循环每一个字符
            num = num * 10 + ord(i) - ord('0')
        return num

    def atoi3(self, a):
        """
        eval()是用来运算表达式的，你可以试一试
        :param a:
        :return:
        """
        return eval('{a} * 1'.format(a=a))

    def atoi4(self, a):
        """
        结合2，使用lambda与reduce一行解决
        :param a:
        :return:
        """
        return reduce(lambda num, v: num * 10 + ord(v) - ord('0'), a, 0)


if __name__ == '__main__':
    a = "12345"

    solution = Solution()
    result = solution.atoi1(a)
    print(result)
    result = solution.atoi2(a)
    print(result)
    result = solution.atoi3(a)
    print(result)
    result = solution.atoi4(a)
    print(result)

# """
# 分析:
#
# """
