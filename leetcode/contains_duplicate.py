# """
# 题目：判断是否有重复的数
# Given an array of integers, find if the array contains any duplicates.
#
# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
#
# Example 1:
#
# Input: [1,2,3,1]
# Output: true
# Example 2:
#
# Input: [1,2,3,4]
# Output: false
# Example 3:
#
# Input: [1,1,1,3,3,4,3,2,4,2]
# Output: true
#
# """
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)


if __name__ == '__main__':
    a = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

    solution = Solution()
    result = solution.containsDuplicate(a)
    print(result)

# """
# 分析:
#
# """
