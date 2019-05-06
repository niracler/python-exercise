# """
# 题目：You are climbing a stair case. It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps. 
# In how many distinct ways can you climb to the top?
# Note: Given n will be a positive integer.
# Example 1:

# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
#
# """

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [1, 2]  # 到达第一层的方法有1种， 到达第二层的方法有2种
        for i in range(2, n):
            dp.append(dp[i - 1] + dp[i - 2])

        return dp[n]


if __name__ == '__main__':
    a = 2

    solution = Solution()
    result = solution.climbStairs(a)
    print(result)

# """
# 分析: 原来这种像是排列组合的题就是动态规划了么？
# 我们来看倒数第一步， 
# 如果用 dp[i] 表示达到第 i 层楼梯的所有方法，
# 那么它进一步等于到达第 i-1 层楼梯的方法加上到达第 i-2 层楼梯的方法的和， 
# 即 dp[i] = dp[i-1] + dp[i-2]   
#
# """
