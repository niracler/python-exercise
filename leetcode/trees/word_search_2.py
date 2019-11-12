# """
# 题目：Given a 2D board and a list of words from the dictionary, find all words in the board.
#
# Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
#
#
#
# Example:
#
# Input:
# board = [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
# words = ["oath","pea","eat","rain"]
#
# Output: ["eat","oath"]
#
# Note:
#
# All inputs are consist of lowercase letters a-z.
# The values of words are distinct.
#
# url:https://leetcode.com/problems/word-search-ii/
# """

import collections
from typing import List


class Solution:
    def __init__(self):
        self.dx = [-1, 1, 0, 0]
        self.dy = [0, 0, -1, 1]
        self.END_OF_WORD = '#'

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ## 假如是空
        if not board or not board[0]: return []
        if not words: return []

        self.result = set()

        # 建立trie树
        root = collections.defaultdict()
        for word in words:
            node = root
            for char in word:
                node = node.setdefault(char, collections.defaultdict())

            node[self.END_OF_WORD] = self.END_OF_WORD

        # 矩阵的长宽
        self.m, self.n = len(board), len(board[0])

        # 遍历这个图，找开头那个字母
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] in root:
                    self._dfs(board, i, j, "", root)

        return list(self.result)

    def _dfs(self, board, i, j, cur_word, cur_dict):
        cur_word += board[i][j]  # 当前拼出来的单词
        cur_dict = cur_dict[board[i][j]]  # 当前的可选项

        if self.END_OF_WORD in cur_dict:
            self.result.add(cur_word)

        tmp, board[i][j] = board[i][j], '@'

        for k in range(4):
            x, y = i + self.dx[k], j + self.dy[k]
            if 0 <= x < self.m and 0 <= y < self.n \
                    and board[x][y] != '@' and board[x][y] in cur_dict:
                self._dfs(board, x, y, cur_word, cur_dict)

        board[i][j] = tmp


if __name__ == '__main__':
    board = [
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v']
    ]
    words = ["a", "pea", "eat", "rain"]

    solution = Solution()
    result = solution.findWords(board, words)
    print(result)

# """
# 分析:
# 1. dfs 太慢了
# 2. trei树
#
# """
