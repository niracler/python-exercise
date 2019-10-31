# """
# 题目：Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]
#
# url:https://leetcode.com/problems/generate-parentheses/
# """
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        self._gen(0, 0, n, "")

        return self.res

    def _gen(self, left, right, n, result):
        """
        通过搜索的方法生成结果
        :param left: 左括号的使用的数目
        :param right: 右括号的使用的数目
        :param n: 需要生成的括号数
        :param result: 结果
        :return:
        """

        # 假如左右括号使用情况相等，都是目标值，那么就保存结果
        if left == n and right == n:
            self.res.append(result)
            return

        if left < n:
            self._gen(left + 1, right, n, result + "(")  # 尝试放一个左括号
        if left > right and right < n:
            self._gen(left, right + 1, n, result + ")")  # 尝试放一个右括号


if __name__ == '__main__':
    a = 3

    solution = Solution()
    result = solution.generateParenthesis(a)
    print(result)

# """
# 分析:
# 1. 数学归纳法
# 2. 搜索
# 3. 在搜索的基础上的进行剪枝
#
# """
