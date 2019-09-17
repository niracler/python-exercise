# """
# 题目：Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.
#
# Example:
#
# Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
# Output: [3,3,5,5,6,7]
# Explanation:
#
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Note:
# You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.
#
# Follow up:
# Could you solve it in linear time?
#
# url:https://leetcode.com/problems/sliding-window-maximum/
# """
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums: return []

        windows, maxs = [], []  # windows 存的是下标

        # 尝试滑动
        for i, num in enumerate(nums):
            if i >= k and windows[0] <= i - k:
                windows.pop(0)

            # 比刚才进去的小的前面的都弹出来
            while windows != [] and nums[windows[0]] < num:
                windows.pop(0)

            # 比刚才进去的小的后面的都弹出来
            while windows != [] and nums[windows[-1]] < num:
                windows.pop()

            windows.append(i)

            if i >= k-1:
                maxs.append(nums[windows[0]])

        return maxs


if __name__ == '__main__':
    nums = [1, 3, 1, 2, 0, 5]
    k = 3

    solution = Solution()
    result = solution.maxSlidingWindow(nums, k)
    print(result)

# """
# 分析:使用双向队列，比准备进去的小的前面的都弹出来， 比准备进去的小的后面的都弹出来
#
# """
