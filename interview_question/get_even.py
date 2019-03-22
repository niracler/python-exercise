# """
# 题目：该函数的输入是一个仅包含数字的list,输出一个新的list，其中每一个元素要满足以下条件：
#     1、该元素是偶数
#     2、该元素在原list中是在偶数的位置(index是偶数)
#
# """


class Solution:
    def get_even(self, nums):
        """
        [列表中的元素 for in 循环 if 判断语句]
        :param nums:
        :return:
        """
        return [i for i in nums[::2] if i % 2 == 0]


if __name__ == '__main__':
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 7, 9, 10]

    solution = Solution()
    result = solution.get_even(nums)
    print(result)

# """
# 分析:
#
# """
