# """
# 题目：
# Implement strStr().
#
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#
# Example 1:
#
# Input: haystack = "hello", needle = "ll"
# Output: 2
# Example 2:
#
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# Clarification:
#
# What should we return when needle is an empty string? This is a great question to ask during an interview.
#
# For the purpose of this problem, we will return 0 when needle is an empty string.
# This is consistent to C's strstr() and Java's indexOf().
#
# """


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        自己实现的找子串的函数, 使用字符串切片还挺快的，86%， 而且原来leetcode的运算时间是真的有波动的。
        :param haystack:
        :param needle:
        :return:
        """
        if needle == "":
            return 0

        for i in range(len(haystack)-len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i

        return -1



if __name__ == '__main__':
    haystack = "a"
    needle = "a"

    solution = Solution()
    result = solution.strStr(haystack, needle)
    print(result)

# """
# 分析:
#
# """
