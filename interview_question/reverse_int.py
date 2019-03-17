# """
# 题目：
#
# """


class Solution:
    def reverse_int(self, a):
        str_a = str(a)

        if str_a[0] == '-':
            str_a = str_a.split('-')[1]
            int_a = int('-' + str_a[::-1])
        else:
            int_a = int(str_a[::-1])
        return int_a


if __name__ == '__main__':
    a = -214748364749

    solution = Solution()
    result = solution.reverse_int(a)
    print(result)

# """
# 分析:
#
# """
