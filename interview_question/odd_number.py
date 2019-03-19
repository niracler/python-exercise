# """
# 题目： a = [1,2,3,4,5,6,7,8,9,10], 求出列表所有奇数并构造新列表
#
# """


class Solution:
    def odd_number(self, alist):
        """
        列表生成式...
        :param alist:
        :return:
        """
        return [num for num in alist if num % 2 == 1]


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    solution = Solution()
    result = solution.odd_number(a)
    print(result)

# """
# 分析:
#
# """
