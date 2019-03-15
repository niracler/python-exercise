# """
# 题目：请反转字符串 "aStr"?
#
# """


class Solution:
    def reversed_str(self, a_str):
        return a_str[::-1]


if __name__ == '__main__':
    a_str = "aStr"

    solution = Solution()
    result = solution.reversed_str(a_str)
    print(result)

# """
# 分析:
#
# """
