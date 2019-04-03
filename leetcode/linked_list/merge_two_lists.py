# """
# 题目：Merge two sorted linked lists and return it as a new list.
# The new list should be made by splicing together the nodes of the first two lists.
#
# Example:
#
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
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
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        result_list = ListNode(-1)
        tail = result_list

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        tail.next = l1 or l2

        return result_list.next


if __name__ == '__main__':
    l1 = ListNode(5)
    l1.add_node([1, 2, 4])
    # l1.print_node()
    l2 = ListNode(5)
    l2.add_node([1, 3, 4])
    # l2.print_node()

    solution = Solution()
    result = solution.mergeTwoLists(l1.next, l2.next)
    result.print_node()

# """
# 分析: 我没有能力去理解这个链表的结构是什么
#
# """
