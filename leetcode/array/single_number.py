# """
# 题目：
# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
#
# Note:
#
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
#
# Example 1:
#
# Input: [2,2,1]
# Output: 1
# Example 2:
#
# Input: [4,1,2,1,2]
# Output: 4
# """
from typing import List


class Solution:
    def singleNumber2(self, nums: List[int]) -> int:
        """
        这个方法太慢了
        :param nums:
        :return:
        """
        for i in set(nums):
            if nums.count(i) == 1:
                return i

    def singleNumber(self, nums: List[int]) -> int:
        """
        时间复杂度O(n),用一个数组将单个的数装起来
        :param nums:
        :return:
        """
        double_list = []

        for i in nums:
            if i in double_list:
                double_list.remove(i)
            else:
                double_list.append(i)

        return double_list[0]



if __name__ == '__main__':
    alist = [2, 2, 1, 1, 0]

    solution = Solution()
    result = solution.singleNumber2(alist)
    print(result)
    result = solution.singleNumber(alist)
    print(result)

# """
# 分析: list.count, set, 这种函数要少用吧?
#
# """
