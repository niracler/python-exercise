# 关于字典树的模板
ALPHABET_SIZE = 256


class TrieNode:
    def __init__(self):
        self.children = [None] * ALPHABET_SIZE

        # is_end_of_word is True if Node if node represent
        # the end of the word
        self.is_end_of_word = False
