# """
# 题目：
#
# """
import string


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return all([s.count(c) == t.count(c) for c in string.ascii_lowercase])


if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"

    solution = Solution()
    result = solution.isAnagram(s, t)
    print(result)

# """
# 分析:
#
# """
