# """
# 题目：python代码实现删除一个list里面的重复元素
#
# """


class Solution:
    def dist_func1(self, alist):
        """
        使用set集合函数
        :param alist:
        :return:
        """
        return list(set(alist))

    def dist_func2(self, alist):
        """
        将一个列表的数据取出放到另一个列表中，中间作判断
        :param alist:
        :return:
        """

        new_list = []
        for i in alist:
            if i not  in new_list:
                new_list.append(i)

        return new_list

    def dist_func3(self, alist):
        """
        使用字典
        :param alist:
        :return:
        """
        dicts = {}
        dicts = dicts.fromkeys(alist)
        return list(dicts.keys())


if __name__ == '__main__':
    alist = [1, 2, 4, 2, 4, 5, 7, 10, 5, 5, 7, 8, 9, 0, 3]

    solution = Solution()
    result = solution.dist_func1(alist)
    print(result)
    result = solution.dist_func2(alist)
    print(result)
    result = solution.dist_func3(alist)
    print(result)

# """
# 分析:
#
# """
