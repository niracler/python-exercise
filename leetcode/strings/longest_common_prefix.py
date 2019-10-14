# """
# 题目：Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
# url:https://leetcode.com/problems/longest-common-prefix/
# """

from typing import List


class Solution:
    def longestCommonPrefix1(self, strs: List[str]) -> str:
        """
        找字符串的最长公共前缀，那应该怎么找呢
        :param strs:
        :return:
        """

        if not strs: return ""

        min_str = strs[0]  # 最短的字符串
        min_len = len(strs[0])

        for item in strs:
            if len(item) < min_len:
                min_str = item
                min_len = len(item)

        for i in range(min_len):
            tmp = min_str[0:min_len - i]
            flag = True
            for item in strs:
                if tmp != item[0:min_len - i]:
                    flag = False
            if flag:
                return tmp

        return ""

    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        找字符串的最长公共前缀，pythonic
        :param strs:
        :return:
        """

        if not strs: return ""

        shortest = min(strs, key=len)  # 最短的字符串
        min_len = len(shortest)

        for i in range(min_len):
            tmp = shortest[0:min_len - i]
            flag = True
            for item in strs:
                if tmp != item[0:min_len - i]:
                    flag = False
            if flag:
                return tmp

        return ""


if __name__ == '__main__':
    a = ["ca", "a"]

    solution = Solution()
    result = solution.longestCommonPrefix(a)
    print(result)

# """
# 分析:找一个最短的出来，然后由它的最长前缀开始遍历
#
# """
