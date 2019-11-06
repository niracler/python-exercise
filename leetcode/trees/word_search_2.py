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

from typing import List


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        在这里初始化你的数据结构
        """
        self.children = {}

        # is_end_of_word is True if Node if node represent
        # the end of the word
        self.is_end_of_word = False

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        向这棵树插入一个单词
        """
        if not word:
            self.is_end_of_word = True
            return

        if word[0] not in self.children:
            self.children[word[0]] = Trie()
        self.children[word[0]].insert(word[1:])

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        查找这单词
        """
        if not word and self.is_end_of_word == True:
            return True

        if not word or not self.children.get(word[0], False):
            return False

        return self.children[word[0]].search(word[1:])

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        以这个单词开头的字符串
        """

        if not prefix:
            return True

        if not self.children.get(prefix[0], False):
            return False

        return self.children[prefix[0]].startsWith(prefix[1:])


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []

        # 遍历这个图，找开头那个字母
        for i in range(len(board)):
            for j in range(len(board[0])):
                for word in words:
                    if board[i][j] == word[0]:
                        # 找到开头字母了，我们来深搜一下
                        visited = set()
                        visited.add(str(i) + "," + str(j))
                        if self.help_me(board, i, j, visited, word[1:]):
                            res.append(word)
                            words.remove(word)

        return res

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
#
# """
