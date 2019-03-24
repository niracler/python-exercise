# """
# 题目：The count-and-say sequence is the sequence of integers with the first five terms as following:
#
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
#
# Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.
#
# Note: Each term of the sequence of integers will be represented as a string.
#
# Example 1:
#
# Input: 1
# Output: "1"
# Example 2:
#
# Input: 4
# Output: "1211"
#
# """


class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"

        for i in range(n-1):
            result = self.get_next(result)

        return result

    def get_next(self, num: str) -> str:
        """
        生成下一个数字
        :param num:
        :return:
        """

        the_next = ""

        # 计数
        i = 0
        while i < len(num):
            j = 1
            while j + i < len(num):
                if num[i+j] != num[i]:
                    break
                j += 1
            the_next += str(j) + num[i]
            i += j

        return the_next


if __name__ == '__main__':
    n = 4

    solution = Solution()
    result = solution.countAndSay(n)
    print(result)

# """
# 分析:
#
# """
