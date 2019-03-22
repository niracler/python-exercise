# """
# 题目：用一行代码生成[1,4,9,16,25,36,49,64,81,100]
#
# """


class Solution:
    def gen_list(self):
        return [x**2 for x in range(1, 11)]


if __name__ == '__main__':
    solution = Solution()
    result = solution.gen_list()
    print(result)

# """
# 分析:
#
# """
