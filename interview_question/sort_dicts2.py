# """
# 题目：
# 给列表中的字典排序：假设有如下list对象，
# alist=[{"name":"a","age":20},{"name":"b","age":30},{"name":"c","age":25}],
# 将alist中的元素按照age从大到小排序
# alist=[{"name":"a","age":20},{"name":"b","age":30},{"name":"c","age":25}]
#
# """


class Solution:
    def sort_dicts2(self, a):
        return sorted(a, key=lambda x: x["age"], reverse=True)


if __name__ == '__main__':
    a = [{"name": "a", "age": 20}, {"name": "b", "age": 30}, {"name": "c", "age": 25}]

    solution = Solution()
    result = solution.sort_dicts2(a)
    print(result)

# """
# 分析:
#
# """
