# """
# 题目：
# Given an array nums, write a function
# to move all 0's to the end of it
# while maintaining the relative order of the non-zero elements.
#
# Example:
#
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Note:
#
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
#
# """
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0

        while 0 in nums:
            count = count + 1
            nums.remove(0)

        for i in range(0, count):
            nums.append(0)


if __name__ == '__main__':
    alist = [0, 1, 0, 3, 12]

    solution = Solution()
    result = solution.moveZeroes(alist)
    print(alist)

# """
# 分析: 原来不需要排序啊,只需要将nums中的零去到后面
#
# """
