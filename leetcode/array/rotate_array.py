# Given an array, rotate the array to the right by k steps, where k is non-negative.
#
# Example 1:
#
# Input: [1,2,3,4,5,6,7] and k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:
#
# Input: [-1,-100,3,99] and k = 2
# Output: [3,99,-1,-100]
# Explanation:
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
# Note:
#
# Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
# Could you do it in-place with O(1) extra space?

# """
# 题目：
#
# """
from typing import List


class Solution:
    def rotate1(self, nums: List[int], k: int) -> None:
        """
        这是我的方法， 实在是太慢以至于超时了， 时间复杂度是O(n^2)
        :param nums:
        :param k:
        :return:
        """
        n = len(nums)
        for i in range(k):
            tmp = nums[-1]  # 将最后一个存起来

            # 全部向前挪
            for j in range(n-1):
                nums[-j-1] = nums[-j-2]

            nums[0] = tmp

        print(nums)

    def rotate(self, nums: List[int], k: int) -> None:
        """
        使用内置插入函数，虽然过了，只有10%，也是太慢了
        :param nums:
        :param k:
        :return:
        """
        for i in range(k):
            nums.insert(0, nums.pop(-1))

        print(nums)


if __name__ == '__main__':
    alist = [1, 2, 3, 4, 5, 6, 7]
    k = 3

    solution = Solution()
    solution.rotate1(alist, k)

# """
# 分析:
#
# """
