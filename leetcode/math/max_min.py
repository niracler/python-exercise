# """
# 题目：
#
# url:
# """


class Solution:
    def max_min(self, nums):

        if nums[0] > nums[1]:
            nums[0], nums[1] = nums[1], nums[0]
        if nums[0] > nums[2]:
            nums[0], nums[2] = nums[2], nums[0]
        if nums[1] > nums[2]:
            nums[1], nums[2] = nums[2], nums[1]

        return nums


if __name__ == '__main__':
    nums = [1, 12, 3]

    solution = Solution()
    result = solution.max_min(nums)
    print(result)

# """
# 分析:
#
# """
