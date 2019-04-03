# """
# 题目：写一个函数找出一个整数数组中，第二大的数
#
# """


class Solution:
    def find_second_large_num(self, a):
        """
        在找最大的过程中，将第二大也记下来
        :param a:
        :return:
        """
        large_number = a[0]
        second_large_number = a[0]

        for i in a:
            if i > large_number:
                second_large_number = large_number
                large_number = i

        return second_large_number


if __name__ == '__main__':
    a = [68, 4, 35, 46, 843, 54381, 32, 235, 35153, 8, 84579, 43, 51]

    solution = Solution()
    result = solution.find_second_large_num(a)
    print(result)

# """
# 分析:
#
# """
