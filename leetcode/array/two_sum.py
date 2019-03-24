"""

from https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/546/

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        :param nums:
        :param target:
        :return:
        """
        # #这是我的解法,只比15%快,我这里的时间复杂度为O(n^2)
        # for i in range(0, len(nums) - 1):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        #
        # return []

        # 大神的做法, 使用hash表来使时间复杂度降为O(n),hash的结果就是与之互补的另外一个数 40ms 78%
        dicts = {}
        for i in range(0, len(nums)):  # 循环遍历所有数
            cur = nums[i]
            if cur in dicts:
                return [dicts[cur], i]
            dicts[target - cur] = i


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9

    solution = Solution()
    result = solution.twoSum(nums, target)

    print(result)
