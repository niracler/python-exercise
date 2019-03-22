# """
# 题目：两个有序列表，l1,l2，对这两个列表进行合并不可使用extend
#
# """


class Solution:
    def loop_merge_sort(self, l1, l2):
        tmp = []
        while len(l1) > 0 and len(l2) > 0:
            if l1[0] < l2[0]:
                tmp.append(l1[0])
                del l1[0]
            else:
                tmp.append(l2[0])
                del l2[0]


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7, 8]
    b = [3, 4, 5, 6, 7, 10, 20, 30]

    solution = Solution()
    result = solution.loop_merge_sort(a, b)
    print(result)

# """
# 分析:
#
# """
