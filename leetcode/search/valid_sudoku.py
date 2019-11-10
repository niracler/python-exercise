# """
# 题目：Determine if a 9x9 Sudoku board is valid.
# Only the filled cells need to be validated according to the following rules:
#
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
#
# A partially filled sudoku which is valid.
#
# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
#
# url:https://leetcode.com/problems/valid-sudoku/
# """


from typing import List


class Solution:
    def __init__(self):
        self.board = None
        self.rule1 = None
        self.rule2 = None
        self.rule3 = None

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        只需要现有的数字符合条件即可，不需要真的有解
        :param board:
        :return:
        """
        self.board = board
        self.rule1 = [set([str(i) for i in range(1, 10)]) for i in range(9)]  # 规则1 每一行所剩下的棋子
        self.rule2 = [set([str(i) for i in range(1, 10)]) for i in range(9)]  # 规则2 每一列所剩下的棋子
        self.rule3 = [[set([str(i) for i in range(1, 10)]) for i in range(3)] for i in range(3)]  # 规则3 每一九宫格所剩下的棋子

        # 遍历所有，生成原始图
        try:
            for i in range(9):
                for j in range(9):
                    if self.board[i][j] != '.':
                        self.rule1[i].remove(self.board[i][j])
                        self.rule2[j].remove(self.board[i][j])
                        self.rule3[i // 3][j // 3].remove(self.board[i][j])

        except Exception as e:
            return False

        return True


if __name__ == '__main__':
    a = [
        [".", "8", "7", "6", "5", "4", "3", "2", "1"],
        ["2", ".", ".", ".", ".", ".", ".", ".", "."],
        ["3", ".", ".", ".", ".", ".", ".", ".", "."],
        ["4", ".", ".", ".", ".", ".", ".", ".", "."],
        ["5", ".", ".", ".", ".", ".", ".", ".", "."],
        ["6", ".", ".", ".", ".", ".", ".", ".", "."],
        ["7", ".", ".", ".", ".", ".", ".", ".", "."],
        ["8", ".", ".", ".", ".", ".", ".", ".", "."],
        ["9", ".", ".", ".", ".", ".", ".", ".", "."]
    ]

    solution = Solution()
    result = solution.isValidSudoku(a)
    print(result)

# """
# 分析:
#
# """
