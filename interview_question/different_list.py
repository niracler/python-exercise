# """
# 题目：给定两个列表，怎么找出他们相同的元素和不同的元素？
#
# """


class Solution:
    def different_list(self, list1, list2):
        result = {
            'same': [],
            'different': [],
        }

        list1 = set(list1)
        list2 = set(list2)

        result['same'] = list1 & list2
        result['different'] = list1 ^ list2

        return result


if __name__ == '__main__':
    list1 = [1, 2, 3]
    list2 = [3, 4, 5]

    solution = Solution()
    result = solution.different_list(list1, list2)
    print(result)

# """
# 分析:
#
# """
