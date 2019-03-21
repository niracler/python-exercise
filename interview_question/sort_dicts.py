# """
# 题目：现有字典 d= {'a':24,'g':52,'i':12,'k':33}请按value值进行排序?
#
# """


class Solution:
    def sort_dicts(self, dicts: dict):
        """
        lambda 输入：输出
        :param dicts:
        :return:
        """
        return sorted(dicts.items(), key=lambda x: x[1])


if __name__ == '__main__':
    d = {'a': 24, 'i': 12, 'g': 52, 'k': 33}

    solution = Solution()
    result = solution.sort_dicts(d)
    print(result)

# """
# 分析: lambda 输入：输出 。是用来做匿名函数的
#
# """
