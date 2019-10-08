# """
# 题目：Implement pow(x, n), which calculates x raised to the power n (xn).
#
# Example 1:
#
# Input: 2.00000, 10
# Output: 1024.00000
# Example 2:
#
# Input: 2.10000, 3
# Output: 9.26100
# Example 3:
#
# Input: 2.00000, -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25
# Note:
#
# -100.0 < x < 100.0
# n is a 32-bit signed integer, within the range [−231, 231 − 1]
#
# url:https://leetcode.com/problems/powx-n/
# """


class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        这里的n要考虑到三种情况，大于零，小于零，等于零
        :param x:
        :param n:
        :return:
        """
        # 结束条件
        if not n: return 1

        # 将其拆成左右两半进行计算
        if n > 0:
            result = self.myPow(x, n // 2)
            result *= result
            if n % 2: result *= x  # 奇数的时候
        else:
            result = 1 / self.myPow(x, -n // 2)
            result *= result
            if n % 2: result *= 1 / x  # 奇数的时候

        return result


if __name__ == '__main__':
    x = 2.00000
    n = -1

    solution = Solution()
    result = solution.myPow(x, n)
    print(result)

# """
# 分析:
#   1. 库函数
#   2. 暴力O(n)
#   3. 分治O(log(n)),有递归写法以及循环写法
# """
