# """
# 题目：Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
#
# k is a positive integer and is less than or equal to the length of the linked list.
# If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
#
# Example:
#
# Given this linked list: 1->2->3->4->5
#
# For k = 2, you should return: 2->1->4->3->5
#
# For k = 3, you should return: 3->2->1->4->5
#
# Note:
#
# Only constant extra memory is allowed.
# You may not alter the values in the list's nodes, only nodes itself may be changed.
#
# url:https://leetcode.com/problems/reverse-nodes-in-k-group/
# """

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


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.rever(head, k)

    def rever(self, head, k):

        node = head

        if not head or not head.next:
            return head

        for i in range(0, k):
            if not node:
                return head
            node = node.next

        tmp2 = first = head
        last = head.next
        first.next = None

        for i in range(1, k):
            tmp = first
            first = last
            last = last.next
            first.next = tmp

        tmp2.next = self.rever(last, k)

        return first


if __name__ == '__main__':
    a = ListNode(-1)
    a.add_node([1, 14, 3, 4, 5])
    a.print_node()

    solution = Solution()
    result = solution.reverseKGroup(a.next, 3)
    result.print_node()

# """
# 分析: too hard
#
# """
