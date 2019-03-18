# """
# 题目：
#
# 全字母短句 PANGRAM 是包含所有英文字母的句子，比如：A QUICK BROWN FOX JUMPS OVER THE LAZY DOG.
# 定义并实现一个方法 get_missing_letter, 传入一个字符串采纳数，返回参数字符串变成一个 PANGRAM 中所缺失的字符。
# 应该忽略传入字符串参数中的大小写，返回应该都是小写字符并按字母顺序排序（请忽略所有非 ACSII 字符）
#
# 下面示例是用来解释，双引号不需要考虑:
#
# (0)输入: "A quick brown for jumps over the lazy dog"
# 返回： ""
#
# (1)输入: "A slow yellow fox crawls under the proactive dog"
# 返回: "bjkmqz"
#
# (2)输入: "Lions, and tigers, and bears, oh my!"
# 返回: "cfjkpquvwxz"
#
# (3)输入: ""
# 返回："abcdefghijklmnopqrstuvwxyz"
#
# """


class Solution:
    def get_missing_letter(self, a):
        """使用集合操作"""
        s1 = set("abcdefghijklmnopqrstuvwxyz")
        s2 = set(a)

        return "".join(sorted(s1-s2))

if __name__ == '__main__':
    a = "A slow yellow fox crawls under the proactive dog"

    solution = Solution()
    result = solution.get_missing_letter(a)
    print(result)

# """
# 分析:
#
# """
