# """
# 题目：给定一个任意长度数组，实现一个函数
# 让所有奇数都在偶数前面，而且奇数升序排列，偶数降序排序，如字符串'1982376455',变成'1355798642'
#
# """


class Solution:
    def up_stream(self, a):
        """
        有点蠢，我这里是有多次循环了
        :param a:
        :return:
        """
        odd_num = ""
        even_num = ""
        result = ""

        for i in a:
            if int(i) % 2 == 1:
                odd_num += i  # 将奇数拿出来
            else:
                even_num += i  # 将偶数拿出来

        result += "".join(sorted(odd_num, key=lambda x: int(x)))
        result += "".join(sorted(even_num, key=lambda x: int(x), reverse=True))

        return result


if __name__ == '__main__':
    a = '1982376455'

    solution = Solution()
    result = solution.up_stream(a)
    print(result)

# """
# 分析:
#
# """
