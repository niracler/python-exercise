# """
# 题目：Reverse a singly linked list.
#
# Example:
#
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# Follow up:
#
# A linked list can be reversed either iteratively or recursively.
# Could you implement both?
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
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        cur, prev = head, None

        while cur:
            prev, prev.next, cur = cur, prev, cur.next

        return prev


if __name__ == '__main__':
    a = ListNode(-1)
    a.add_node([1, 2, 3, 4, 5])
    a.print_node()

    solution = Solution()
    result = solution.reverseList(a.next)
    result.print_node()

# """
# 分析:不行，我对python的拷贝的机制不太熟悉
#
# """
