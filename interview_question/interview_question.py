# """
# 题目：给定一个已经降序排列的数组,请编写一个函数,将其重新排列成最小数-最大数-次小数-次大数-第三小数-第三大
# 数-...,依此类推。
#
# 例如,给定 [7, 6, 5, 4, 3, 2, 1] ,则需给出的新排列为 [1, 7, 2, 6, 3, 5, 4] 。
#
# 第二题
# 给定一个 m 行 n 列二维数组中,其中每一行的数字从左到右都是升序排列,每一列的数字从上到下也都是升序排
# 列。请编写一个函数,输入这样的一个二维数组和一个整数,判断二维数组中是否含有该整数。
#
# 例如下面的二维数组就是符合上述描述的。如果在这个数组中查找数字 6,则返回 true;如果查找数字 5,则返回
# false。
#
# 2 4 6 8
# 3 7 9 16
# 12 13 14 19
#
# 第三题
# 如果一个单词通过循环右移获得的单词,我们称这些单词都为一种循环单词。 例如:picture 和 turepic 就是属于同
# 一种循环单词。现在给出 n 个单词,需要统计这 n 个单词中有多少种循环单词。
#
# 例如,给定单词组 ["picture", "turepic", "icturep", "word", "ordw"] ,他们包含了 2 种循环单
# 词,分别是 ["picture", "turepic", "icturep"] 和 ["word", "ordw"] 。这时你的函数应该返回 2。
#
# """


class Solution:
    def quest1(self, a):
        res = []
        for i in range(1, len(a) // 2 + 1):
            res.append(a[-i])
            res.append(a[i - 1])

        if len(a) % 2:
            res.append(a[len(a) // 2])

        return res

    def quest2(self, a, target):
        for nums in a:  # 一行一行二分查找
            left, right = 0, len(nums) - 1
            while left <= right:  # 假如还有搜索范围
                mid = (left + right) // 2

                if target > nums[mid]:
                    left = mid + 1
                elif target < nums[mid]:
                    right = mid - 1
                else:
                    return True

        return False

    def quest3(self, word):
        i = 0
        while i < len(word):
            double_word = word[i] + word[i]
            j = i + 1
            while j < len(word):
                if len(word[i]) == len(word[j]) and word[j] in double_word:
                    del word[j]
                else:
                    j = j + 1
            i = i + 1
        return len(word)


if __name__ == '__main__':
    a1 = [7, 6, 5, 4, 4, 3, 2, 1]
    a2 = [
        [2, 4, 6, 8],
        [3, 7, 9, 16],
        [12, 13, 14, 19]
    ]
    target = 5
    a3 = ["picture", "turepic", "icturep", "word", "ordw"]

    solution = Solution()

    result1 = solution.quest1(a1)
    result2 = solution.quest2(a2, target)
    result3 = solution.quest3(a3)

    print(result1)
    print(result2)
    print(result3)

# """
# 分析:
#
# """
