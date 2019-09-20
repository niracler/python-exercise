# """
# 题目：Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#
# Note:
#
# The solution set must not contain duplicate triplets.
#
# Example:
#
# Given array nums = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
#
# url:https://leetcode.com/problems/3sum/
# """
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        res = set()
        nums.sort()

        #  遍历到倒数第三个
        for (i, num1) in enumerate(nums[:-2]):
            # 假如跟上一个一样，跳过
            if i >= 1 and num1 == nums[i - 1]:
                continue

            hash_map = {}
            # 遍历剩下的
            for num2 in nums[i + 1:]:
                if num2 not in hash_map:  # 现在要看的是你是不是第三个数，你要明白，你的前辈是前两个数
                    hash_map[-num1 - num2] = 1
                else:
                    res.add((num1, num2, -num1 - num2))
        return [*map(list, res)]


if __name__ == '__main__':
    a = [0,0,0,0]

    solution = Solution()
    result = solution.threeSum(a)
    print(result)

# """
# 分析: 排序后再两边夹，我感觉我更喜欢这种方法，因为这要怎么去重啊？
#      想去重的话,好像一定要排序才行
#      那个set是什么操作？？？？？
#
# """
