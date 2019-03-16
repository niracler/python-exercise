# """
# 题目：请写出一段python代码实现删除list里面的重复元素？
#
# """


class Solution:
    def del_same(self, alist):
        return list(set(alist))

if __name__ == '__main__':
    alist = ['b', 'c', 'd', 'c', 'a', 'a']

    solution = Solution()
    result = solution.del_same(alist)
    print(result)

# """
# 分析:
#
# """
