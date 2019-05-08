# """
# 题目：Given an integer array nums,
# find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
#
# Example:
#
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:
#
# If you have figured out the O(n) solution,
# try coding another solution using the divide and conquer approach, which is more subtle.
#
# """


from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        max_val = [nums[0], ]  # 之前最好的结果
        for i in range(1, len(nums)):
            max_val.append(max(nums[i], max_val[i - 1] + nums[i]))
        return max(max_val)

if __name__ == '__main__':
    a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

    solution = Solution()
    result = solution.maxSubArray(a)
    print(result)

# """
# 分析:
#
# """
