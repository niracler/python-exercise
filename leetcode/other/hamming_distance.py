# """
# 题目：The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
#
# Given two integers x and y, calculate the Hamming distance.
#
# Note:
# 0 ≤ x, y < 231.
#
# Example:
#
# Input: x = 1, y = 4
#
# Output: 2
#
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
#
# The above arrows point to positions where the corresponding bits are different.
#
# """


class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        count = 0
        while x or y:
            count += abs((x % 2) - (y % 2))
            x //= 2
            y //= 2

        return count


if __name__ == '__main__':
    x = 1
    y = 4

    solution = Solution()
    result = solution.hammingDistance(x, y)
    print(result)

# """
# 分析:
#
# """
