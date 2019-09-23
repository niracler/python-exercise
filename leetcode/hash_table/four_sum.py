# """
# 题目：Given an array nums of n integers and an integer target,
# are there elements a, b, c, and d in nums such that a + b + c + d = target?
# Find all unique quadruplets in the array which gives the sum of target.
#
# Note:
#
# The solution set must not contain duplicate quadruplets.
#
# Example:
#
# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
#
# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]
#
# url:https://leetcode.com/problems/4sum/
# """
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []

        res = set()
        nums.sort()

        #  遍历到倒数第4个
        for (i, num1) in enumerate(nums[:-3]):
            # 假如跟上一个一样，跳过
            if i >= 1 and num1 == nums[i - 1]:
                continue

            for (j, num2) in enumerate(nums[i + 1: -2]):
                hash_map = {}
                # 遍历剩下的
                for num3 in nums[i + j + 2:]:
                    if num3 not in hash_map:  # 现在要看的是你是不是第三个数，你要明白，你的前辈是前两个数
                        hash_map[target - num1 - num2 - num3] = 1
                    else:
                        res.add((num1, num2, num3, target - num1 - num2 - num3))
        return [*map(list, res)]


if __name__ == '__main__':
    a = [-3, -1, 0, 2, 4, 5]

    solution = Solution()
    result = solution.fourSum(a, 0)
    print(result)

# """
# 分析:
#
# """
