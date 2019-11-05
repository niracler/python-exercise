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

        # return self.help_me(0, 0)  # 我们来玩数独吧，请帮我, 第一行第一个放个1

    def help_me(self, x, y):
        """
        我们先来遍历每一个格,
        这种方法是不行的，因为一旦成功放下之后就不再改变了？？？
        :param x:
        :param y:
        :return:
        """
        # 结束条件
        if not (x < 9 and y < 9):
            return True

        # 从这里进来的都是第一次进的
        # 这个格子有的放么？
        if self.board[x][y] == '.':
            # 有位置放，尝试一下是否能放进去
            myset = self.rule1[x] & self.rule2[y] & self.rule3[x // 3][y // 3]

            if not myset:  # 换一个里面有的数
                return False

            for i in range(1, 10):
                # print("x = " + str(x) + ", y = " + str(y) + ", i =  " + str(i))
                if str(i) in myset:  # 1-9都试试
                    tmp = str(i)
                    self.board[x][y] = tmp
                    self.rule1[x].remove(tmp)
                    self.rule2[y].remove(tmp)
                    self.rule3[x // 3][y // 3].remove(tmp)

                    # 看一下行不行
                    if y < 8:
                        flag = self.help_me(x, y + 1)
                    else:
                        flag = self.help_me(x + 1, 0)

                    if not flag:  # 假如失败了
                        self.board[x][y] = '.'
                        self.rule1[x].add(tmp)
                        self.rule2[y].add(tmp)
                        self.rule3[x // 3][y // 3].add(tmp)
                    else:
                        return True

        else:
            pass

        # 遍历所有格子
        if y < 8:
            flag = self.help_me(x, y + 1)
        else:
            flag = self.help_me(x + 1, 0)

        return flag


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
