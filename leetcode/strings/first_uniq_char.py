# """
# 题目：
#
# """


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = {}

        for char in s:
            if char in counter:
                counter[char] += 1
            else:
                counter[char] = 1

        for i in range(len(s)):
            if counter[s[i]] == 1:
                return i

        return -1


if __name__ == '__main__':
    s = "leetcode"

    solution = Solution()
    result = solution.firstUniqChar(s)
    print(result)

# """
# 分析:
#
# """
