# """
# 题目：Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
# Note: For the purpose of this problem, we define empty string as valid palindrome.
#
# Example 1:
#
# Input: "A man, a plan, a canal: Panama"
# Output: true
# Example 2:
#
# Input: "race a car"
# Output: false
#
# """


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        找英文回文
        :param s:
        :return:
        """

        # 预处理
        s = s.lower()
        s = ''.join([x for x in s if x.isalnum()])

        for i in range(int(len(s) / 2)):
            if s[i] != s[-i-1]:
                return False

        return True


if __name__ == '__main__':
    a = "0p"

    solution = Solution()
    result = solution.isPalindrome(a)
    print(result)

# """
# 分析:
#
# """
