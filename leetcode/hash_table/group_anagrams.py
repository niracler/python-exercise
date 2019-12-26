# """
# 题目：Given an array of strings, group anagrams together.
#
# Example:
#
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note:
#
# All inputs will be in lowercase.
# The order of your output does not matter.
#
# url:https://leetcode.com/problems/group-anagrams/
# """
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        num = {
            "a": 2,
            "b": 3,
            "c": 5,
            "d": 7,
            "e": 11,
            "f": 13,
            "g": 17,
            "h": 19,
            "i": 23,
            "j": 29,
            "k": 31,
            "l": 37,
            "m": 41,
            "n": 43,
            "o": 47,
            "p": 53,
            "q": 59,
            "r": 61,
            "s": 67,
            "t": 71,
            "u": 73,
            "v": 79,
            "w": 83,
            "x": 89,
            "y": 97,
            "z": 101,
        }
        res = {}
        for istr in strs:
            key = 1
            for i in istr:
                key *= num[i]
            if key in res:
                res[key].append(istr)
            else:
                res[key] = [istr]

        return list(res.values())


if __name__ == '__main__':
    a = ["eat", "tea", "tan", "ate", "nat", "bat"]

    solution = Solution()
    result = solution.groupAnagrams(a)
    print(result)

# """
# 分析: 使用质数相乘的方法就很棒了，我一开始想用位数相加的，但是对这种一个字母出现多次的无效
#
# """
