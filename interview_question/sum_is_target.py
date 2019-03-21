# """
# 题目：给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
# 你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。
# 示例:给定nums = [2,7,11,15],target=9 因为 nums[0]+nums[1] = 2+7 =9,所以返回[0,1]
#
# """


class Solution:
    def two_sum(self, nums, target):
        """
        传统的直觉算法
        :param nums:
        :param target:
        :return:
        """
        for i in range(len(nums) - 1):
            if nums[i] <= target:
                for j in range(i, len(nums)):
                    if nums[i] + nums[j] == target:
                        return [i, j]

        return []

    def better_two_sum(self, nums, target):
        """
        hash算法
        :param nums:
        :param target:
        :return:
        """
        dicts = {}
        for i in range(len(nums)):
            if nums[i] in dicts:  # 假如对应的数在字典里，则输出
                return [dicts[nums[i]], i]
            dicts[target - nums[i]] = i  # 没有则放进去，等待对应的数的到来


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9

    solution = Solution()
    result = solution.two_sum(nums, target)
    print(result)
    result = solution.better_two_sum(nums, target)
    print(result)

# """
# 分析:
#
# """
