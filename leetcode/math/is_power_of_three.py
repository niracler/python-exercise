# """
# 题目：Given an integer, write a function to determine if it is a power of three.
#
# Example 1:
#
# Input: 27
# Output: true
# Example 2:
#
# Input: 0
# Output: false
# Example 3:
#
# Input: 9
# Output: true
# Example 4:
#
# Input: 45
# Output: false
# Follow up:
# Could you do it without using any loop / recursion?
#
# """


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """

        while n > 1 and n % 3 == 0:
            n //= 3

        if n == 1:
            return True
        else:
            return False


if __name__ == '__main__':
    a = 45

    solution = Solution()
    result = solution.isPowerOfThree(a)
    print(result)

# """
# 分析:
#
# """
