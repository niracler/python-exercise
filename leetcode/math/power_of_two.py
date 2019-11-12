# """
# 题目：
# Given an integer, write a function to determine if it is a power of two.
#
# Example 1:
#
# Input: 1
# Output: true
# Explanation: 20 = 1
# Example 2:
#
# Input: 16
# Output: true
# Explanation: 24 = 16
# Example 3:
#
# Input: 218
# Output: false
# Accepted
#
# url:https://leetcode.com/problems/power-of-two/
# """


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and not (n & n - 1)


if __name__ == '__main__':
    a = 255

    solution = Solution()
    result = solution.isPowerOfTwo(a)
    print(result)

# """
# 分析: 因为二的n次方的二进制是只有一个一，其余都是零
#
# """
