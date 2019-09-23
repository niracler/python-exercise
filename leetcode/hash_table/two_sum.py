# """
# 题目：Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
#
# url:https://leetcode.com/problems/two-sum/
# """
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for i in range(0, len(nums)):
            cur = nums[i]
            if cur in hash_map:
                return [hash_map[cur], i]
            hash_map[target - cur] = i


if __name__ == '__main__':
    a = [2, 7, 11, 15]
    target = 9

    solution = Solution()
    result = solution.twoSum(a, target)
    print(result)

# """
# 分析:
#
# """
