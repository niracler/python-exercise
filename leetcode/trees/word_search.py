# """
# 题目：Given a 2D board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell, w
# here "adjacent" cells are those horizontally or vertically neighboring.
# The same letter cell may not be used more than once.
#
# Example:
#
# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
#
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.
# url: https://leetcode.com/problems/word-search/
# """
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 遍历这个图，找开头那个字母
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    # 找到开头字母了，我们来深搜一下
                    visited = set()
                    visited.add(str(i) + "," + str(j))
                    if self.help_me(board, i, j, visited, word[1:]):
                        return True

        return False

    def help_me(self, board, x, y, visited, word):
        if not word:
            return True

        if x - 1 >= 0 and board[x - 1][y] == word[0] and (str(x - 1) + "," + str(y) not in visited):  # 上
            visited.add(str(x - 1) + "," + str(y))
            if self.help_me(board, x - 1, y, visited, word[1:]):
                return True
            else:
                visited.remove(str(x - 1) + "," + str(y))

        if x + 1 < len(board) and board[x + 1][y] == word[0] and (str(x + 1) + "," + str(y) not in visited):  # 下
            visited.add(str(x + 1) + "," + str(y))
            if self.help_me(board, x + 1, y, visited, word[1:]):
                return True
            else:
                visited.remove(str(x + 1) + "," + str(y))

        if y - 1 >= 0 and board[x][y - 1] == word[0] and (str(x) + "," + str(y - 1) not in visited):  # 左
            visited.add(str(x) + "," + str(y - 1))
            if self.help_me(board, x, y - 1, visited, word[1:]):
                return True
            else:
                visited.remove(str(x) + "," + str(y - 1))

        if y + 1 < len(board[0]) and board[x][y + 1] == word[0] and (str(x) + "," + str(y + 1) not in visited):  # 右
            visited.add(str(x) + "," + str(y + 1))
            if self.help_me(board, x, y + 1, visited, word[1:]):
                return True
            else:
                visited.remove(str(x) + "," + str(y + 1))


if __name__ == '__main__':
    board = [["a", "b"]]

    word1 = "ab"  # return true.
    word2 = "SEE"  # return true.
    word3 = "ABCB"  # return false.

    solution = Solution()

    result1 = solution.exist(board, word1)
    print(result1)

    result2 = solution.exist(board, word2)
    print(result2)

    result3 = solution.exist(board, word3)
    print(result3)

# """
# 分析:我们先来暴力搜索吧！！！
#
# """
