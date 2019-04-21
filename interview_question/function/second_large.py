# """
# 题目：
#
# """


class Solution:
    def get_second(self, a):
        max = a[0]
        second_max = max

        for i in range(0, len(a)):
            if max < a[i]:
                second_max = max
                max = a[i]

        return second_max


if __name__ == '__main__':
    a = [685,43,52,485,634,35,43,88,543,51,63,85,135,814,83,51,35]
    b = [8,8,8,8,8]

    solution = Solution()
    result = solution.get_second(b)

    print(result)

# """
# 分析:
#
# """
