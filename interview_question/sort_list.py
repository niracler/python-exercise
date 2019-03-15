# """
# 题目：请按alist中元素的age由大到小排序
#
# """


class Solution:
    def sort_list(self, alist):
        return sorted(alist, key=lambda x: x['age'], reverse=True)


if __name__ == '__main__':
    alist = [{'name': 'a', 'age': 20}, {'name': 'b', 'age': 30}, {'name': 'c', 'age': 25}]

    solution = Solution()
    result = solution.sort_list(alist)
    print(result)

# """
# 分析:
#
# """
