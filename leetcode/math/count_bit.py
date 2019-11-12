# """
# 题目：
# Given a non negative integer number num.
# For every numbers i in the range 0 ≤ i ≤ num calculate the number of
# 1's in their binary representation and return them as an array.
#
# Example 1:
#
# Input: 2
# Output: [0,1,1]
# Example 2:
#
# Input: 5
# Output: [0,1,1,2,1,2]
# Follow up:
#
# It is very easy to come up with a solution with run time O(n*sizeof(integer)).
# But can you do it in linear time O(n) /possibly in a single pass?
# Space complexity should be O(n).
# Can you do it like a boss?
# Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
#
# url:https://leetcode.com/problems/counting-bits/
# """


class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """

        bits = [0]
        for i in range(1, num + 1):
            bits.append(0)
            bits[i] += bits[i & (i - 1)] + 1

        return bits


if __name__ == '__main__':
    a = 80

    solution = Solution()
    result = solution.countBits(a)
    print(result)

# """
# 分析:
# 1. 遍历，然后计算每个数
# 2. count[n+1]
#
# """
