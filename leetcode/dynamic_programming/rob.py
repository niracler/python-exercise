# """
# 题目：
#
# """
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) <= 2:
            return max(nums)

        max_res = [nums[0], max(nums[0], nums[1])]  # 之前最好的结果
        max_val = [nums[0], nums[1]]  # 之前的结果
        for i in range(2, len(nums)):
            max_val.append(max(nums[i], max_res[i - 2] + nums[i]))
            max_res.append(max(max_val[i], max_res[i - 1]))
            # print(max_res)
        return max(max_val)


if __name__ == '__main__':
    a = [1, 1, 1, 2]

    solution = Solution()
    result = solution.rob(a)
    print(result)

# """
# 分析:
#
# """
