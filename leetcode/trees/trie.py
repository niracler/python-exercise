# """
# 题目：Implement a trie with insert, search, and startsWith methods.
# 应该就是实现一个字典树
#
# url:https://leetcode.com/problems/implement-trie-prefix-tree/
# """


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


if __name__ == '__main__':
    # Your Trie object will be instantiated and called as such:
    trie = Trie()

    trie.insert("apple")
    print(trie.search("apple"))  # returns true
    print(trie.search("app"))  # returns false
    print(trie.startsWith("app"))  # returns true
    trie.insert("app")
    print(trie.search("app"))  # returns true
    print(trie.search("apple"))  # returns true
    print(trie.search("appl"))  # return False

# """
# 分析:使用字典会更快
#
# """
