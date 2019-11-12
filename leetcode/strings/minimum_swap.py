# """
# 题目：You are given two strings s1 and s2 of equal length consisting of letters "x" and "y" only.
# Your task is to make these two strings equal to each other.
# You can swap any two characters that belong to different strings,
# which means: swap s1[i] and s2[j].
#
# Return the minimum number of swaps required to make s1 and s2 equal, or return -1 if it is impossible to do so.
#
#
#
# Example 1:
#
# Input: s1 = "xx", s2 = "yy"
# Output: 1
# Explanation:
# Swap s1[0] and s2[1], s1 = "yx", s2 = "yx".
# Example 2:
#
# Input: s1 = "xy", s2 = "yx"
# Output: 2
# Explanation:
# Swap s1[0] and s2[0], s1 = "yy", s2 = "xx".
# Swap s1[0] and s2[1], s1 = "xy", s2 = "xy".
# Note that you can't swap s1[0] and s1[1] to make s1 equal to "yx", cause we can only swap chars in different strings.
# Example 3:
#
# Input: s1 = "xx", s2 = "xy"
# Output: -1
# Example 4:
#
# Input: s1 = "xxyyxyxyxx", s2 = "xyyxyxxxyx"
# Output: 4
#
#
# Constraints:
#
# 1 <= s1.length, s2.length <= 1000
# s1, s2 only contain 'x' or 'y'.
#
# url:
# """


class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        self.s1 = s1
        self.s2 = s2

        for i in range(len(s1)):
            for j in range(len(s1)):
                print(i, j)  # 遍历所有交换情况
        return 0

    def help_me(self, x, y, step):
        """
        交换 xy 看看行不行
        :param x:
        :param y:
        :return:
        """

        for value, i in enumerate(self.s1):
            self.help_me(x, y, step)

        return 0


if __name__ == '__main__':
    s1 = "xx"
    s2 = "xy"

    solution = Solution()
    result = solution.minimumSwap(s1, s2)
    print(result)

# """
# 分析: 最少的交换次数将两个字符串变成相等
#
# """
