# """
# 题目：
#
# """
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        for i in range(int(len(s) / 2)):
            s[i], s[-i - 1] = s[-i - 1], s[i]

        print(s)


if __name__ == '__main__':
    a = ["h", "e", "l", "l", "o"]

    solution = Solution()
    solution.reverseString(a)

# """
# 分析:
#
# """
