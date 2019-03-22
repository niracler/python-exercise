# """
# 题目：
#
# """


class Solution:
    def reverse(self, x: int) -> int:
        str_x = str(x)

        if str_x[0] == '-':
            str_x = str_x.split('-')[1]
            x = -int(str_x[::-1])
        else:
            x = int(str_x[::-1])

        if not -2 ** 31 < x < 2 ** 31 - 1:
            return 0
        else:
            return x


if __name__ == '__main__':
    a = -3540

    solution = Solution()
    result = solution.reverse(a)
    print(result)

# """
# 分析:
#
# """
