# """
# 题目：You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example:
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
#
# url:https://leetcode.com/problems/add-two-numbers/
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
        node = self

        while node:
            print(node.val)
            node = node.next

    def add_node(self, items: list):
        cur = self
        for item in items:
            cur.next = ListNode(item)
            cur = cur.next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur = l1
        while l2:
            cur.val = l2.val + cur.val

            if (cur.val >= 10 and not cur.next) or (not cur.next and l2.next):
                cur.next = ListNode(0)

            if cur.val >= 10:
                cur.val = cur.val % 10
                cur.next.val += 1

            cur = cur.next
            l2 = l2.next

        while cur:
            if cur.val >= 10 and not cur.next:
                cur.next = ListNode(0)

            if cur.val >= 10:
                cur.val = cur.val % 10
                cur.next.val += 1
            cur = cur.next

        return l1


if __name__ == '__main__':
    l1 = ListNode(9)
    l1.add_node([9])
    l2 = ListNode(9)

    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)
    result.print_node()

# """
# 分析:
#
# """
