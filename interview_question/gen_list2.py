# """
# 题目：使用单一的列表生成式来产生一个新的列表
# 该列表只包含满足以下条件的值，元素为原始列表中偶数切片
#
# """


class Solution:
    def gen_list(self, nums):
        return [i for i in nums if i % 2 == 0]


if __name__ == '__main__':
    nums = [1, 2, 5, 8, 10, 3, 18, 6, 20]

    solution = Solution()
    result = solution.gen_list(nums)
    print(result)

# """
# 分析:
#
# """
