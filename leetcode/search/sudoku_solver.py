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

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        只需要现有的数字符合条件即可，不需要真的有解
        :param board:
        :return:
        """
        self.board = board
        self.help_me()

        print(self.board)

        return

    def help_me(self):
        """
        我们先来遍历每一个格,
        这种方法是不行的，因为一旦成功放下之后就不再改变了？？？
        :param x:
        :param y:
        :return:
        """
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == '.':  # 找到第一个是"."的数
                    for num in range(1, 10):
                        if self.is_valid(i, j, str(num)):
                            self.board[i][j] = str(num)
                            if self.help_me():
                                return True
                            else:
                                self.board[i][j] = "."

                    return False

        return True

    def is_valid(self, x, y, num):
        for i in range(9):
            if self.board[x][i] == num: return False  # 规则1
            if self.board[i][y] == num: return False  # 规则2
            if self.board[3 * (x // 3) + i // 3][3 * (y // 3) + i % 3] == num: return False  # 规则3

        return True


if __name__ == '__main__':
    a = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]

    solution = Solution()
    result = solution.solveSudoku(a)
    print(result)

# """
# 分析:
#
# """
