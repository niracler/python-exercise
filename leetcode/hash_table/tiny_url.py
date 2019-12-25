# """
# 题目：
#
# TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and
# it returns a short URL such as http://tinyurl.com/4e9iAk.
#
# Design the encode and decode methods for the TinyURL service.
# There is no restriction on how your encode/decode algorithm should work.
# You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.
#
# url:https://leetcode.com/problems/encode-and-decode-tinyurl/
# """
import random


class Codec:
    def __init__(self):
        self.tiny_urls = {}

    def encode(self, L: str) -> str:
        num_form = random.randint(1, 1E10)
        while num_form in self.tiny_urls:
            num_form = random.randint(1, 1E10)
        self.tiny_urls[num_form] = L
        return 'http://tinyurl.com/' + str(num_form)

    def decode(self, S: str) -> str:
        return self.tiny_urls[int(S[19:])]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))


if __name__ == '__main__':
    url = "https://leetcode.com/problems/design-tinyurl"

    codec = Codec()
    codec.decode(codec.encode(url))
    print(url)

# """
# 分析:
#
# """
