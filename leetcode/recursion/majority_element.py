# """
# 题目：Given an array of size n, find the majority element.
# The majority element is the element that appears more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element always exist in the array.
#
# Example 1:
#
# Input: [3,2,3]
# Output: 3
# Example 2:
#
# Input: [2,2,1,1,1,2,2]
# Output: 2
#
# url:https://leetcode.com/problems/majority-element/
# """
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        当然是尝试一下自己的方法,虽然是过了，但也太慢了
        :param nums:
        :return:
        """
        map_nums = {}
        len_nums = len(nums)

        for i in range(len_nums):
            if nums[i] in map_nums:
                map_nums[nums[i]] += 1
            else:
                map_nums[nums[i]] = 1
            if map_nums[nums[i]] >= len_nums / 2:
                return nums[i]


if __name__ == '__main__':
    a = [2, 2, 1, 1, 1, 2, 2]

    solution = Solution()
    result = solution.majorityElement(a)
    print(result)

# """
# 分析:
#
# """
