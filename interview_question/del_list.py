# """
# 题目：
#
# """


class Solution:
    def del_from_list(self, alist, a):
        """alist[:]算是alist的拷贝"""
        for item in alist[:]:
            if item == a:
                alist.remove(item)

        return alist


if __name__ == '__main__':
    a = ""
    alist = ["", "", "", "8", 635]

    solution = Solution()
    result = solution.del_from_list(alist, a)
    print(result)

# """
# 分析:
#
# """
