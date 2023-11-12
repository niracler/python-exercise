# """
# 题目：打乱一个排好序的list对象alist？
#
# """

import random


class Solution:
    def radom_a_list(self, alist):
        """
        打乱一个排好序的list对象alist
        :param alist:
        :return:
        """
        random.shuffle(alist)
        return alist


if __name__ == '__main__':
    alist = [1, 2, 3, 4, 5]

    solution = Solution()
    result = solution.radom_a_list(alist)
    print(result)
