# """
# 题目：
#
# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
#
# The digits are stored such that the most significant digit
# is at the head of the list, and each element in the array contain a single digit.
#
# You may assume the integer does not contain any leading zero, except the number 0 itself.
#
# Example 1:
#
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Example 2:
#
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
#
# """

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        好猥琐,这是转为int加一,然后再转为list的
        :param digits:
        :return:
        """
        str_digits = ""
        for i in digits:
            str_digits = str_digits + str(i)

        str_digits = str(int(str_digits) + 1)
        result = []
        for i in str_digits:
            result.append(int(i))

        return result


if __name__ == '__main__':
    alist = [1, 2, 3]

    solution = Solution()
    result = solution.plusOne(alist)
    print(result)

# """
# 分析:
#
# """
