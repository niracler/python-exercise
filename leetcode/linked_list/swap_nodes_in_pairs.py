# """
# 题目：Given a linked list, swap every two adjacent nodes and return its head.
#
# You may not modify the values in the list's nodes, only nodes itself may be changed.
#
# Example:
#
# Given 1->2->3->4, you should return the list as 2->1->4->3.
#
# url:https://leetcode.com/problems/swap-nodes-in-pairs/
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


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        true_head = ListNode(999)
        true_head.next = head
        node = true_head

        while node and node.next and node.next.next:
            one = node.next
            second = node.next.next

            one.next = second.next
            second.next = one
            node.next = second
            node = second.next

        return true_head


if __name__ == '__main__':
    a = ListNode(5)
    a.add_node([1, 2, 3, 4])
    a.print_node()

    solution = Solution()
    result = solution.swapPairs(a.next)
    result.print_node()

# """
# 分析: 主要是我要对这链表结构进行揣测，就很麻烦
#
# """
