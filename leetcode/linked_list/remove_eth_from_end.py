# """
# 题目：Given a linked list, remove the n-th node from the end of list and return its head.
#
# Example:
#
# Given linked list: 1->2->3->4->5, and n = 2.
#
# After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
#
# Given n will always be valid.
#
# Follow up:
#
# Could you do this in one pass?
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
    def deletenode(self, head, num, b=1):
        if num == 0:
            return head.next
        head_tmp = head
        while head and head.next:
            if num == b:
                head.next = head.next.next
            head = head.next
            b += 1
        return head_tmp

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        count = 1
        head_tmp = head
        while head and head.next:
            count += 1
            head = head.next
        index = count - n
        res = self.deletenode(head_tmp, index)
        return res


if __name__ == '__main__':
    l1 = ListNode(2)
    l1.add_node([4])

    solution = Solution()
    l1.print_node()
    result = solution.removeNthFromEnd(l1, 1)
    # print(result)
    result.print_node()

# """
# 分析:
#
# """
