# """
# 题目：Given a singly linked list, determine if it is a palindrome.
#
# Example 1:
#
# Input: 1->2
# Output: false
# Example 2:
#
# Input: 1->2->2->1
# Output: true
# Follow up:
# Could you do it in O(n) time and O(1) space?
#
# """


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def print_node(self):
        """

        :param node: ListNode
        :return:
        """
        node = self.next

        while node:
            print(node.val)
            node = node.next

    def add_node(self, items: list):
        cur = self
        for item in items:
            cur.next = ListNode(item)
            cur = cur.next


class Solution(object):
    def isPalindrome(self, head):
        """
        时间复杂度O(1)怎么弄？
        :type head: ListNode
        :rtype: bool
        """
        node = head
        my_list = []  # 用来装数字的列表
        while node:
            my_list.append(node.val)
            node = node.next

        n = len(my_list)
        for i in range(int(n / 2)):
            if my_list[i] != my_list[n - i - 1]:
                return False

        return True


if __name__ == '__main__':
    l1 = ListNode(2)
    l1.add_node([9])

    solution = Solution()
    result = solution.isPalindrome(l1.next)
    print(result)

# """
# 分析:
#
# """
