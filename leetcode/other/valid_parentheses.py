# """
# 题目：Given a string containing just the characters
# '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.
#
# Example 1:
#
# Input: "()"
# Output: true
# Example 2:
#
# Input: "()[]{}"
# Output: true
# Example 3:
#
# Input: "(]"
# Output: false
# Example 4:
#
# Input: "([)]"
# Output: false
# Example 5:
#
# Input: "{[]}"
# Output: true
#
# """


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        dic = {')': '(', '}': '{', ']': '['}
        l = []

        for c in s:
            if c in dic:
                if len(l) == 0 or dic[c] != l.pop():
                    return False
            else:
                l.append(c)

        return len(l) == 0



if __name__ == '__main__':
    a = "([)]"

    solution = Solution()
    result = solution.isValid(a)
    print(result)

# """
# 分析:
#
# """
