# """
# 题目：写一个列表生成式，产生一个公差为11的等差数列
#
# """


class Solution:
    def gen_list(self):
        return [x * 11 for x in range(10)]


if __name__ == '__main__':
    solution = Solution()
    result = solution.gen_list()
    print(result)

# """
# 分析:
#
# """
