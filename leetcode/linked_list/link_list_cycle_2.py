# """
# 题目：Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
#
# To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in
# the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
#
# Note: Do not modify the linked list.
#
# Example 1:
#
# Input: head = [3,2,0,-4], pos = 1
# Output: tail connects to node index 1
# Explanation: There is a cycle in the linked list, where tail connects to the second node.
#
# Example 2:
#
# Input: head = [1,2], pos = 0
# Output: tail connects to node index 0
# Explanation: There is a cycle in the linked list, where tail connects to the first node.
#
# Example 3:
#
# Input: head = [1], pos = -1
# Output: no cycle
# Explanation: There is no cycle in the linked list.
#
# url:https://leetcode.com/problems/linked-list-cycle-ii/
# """

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

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
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None

        hash_map = {}

        node = head

        while node:
            if node in hash_map:
                return node
            hash_map[node] = 1
            node = node.next

        return None


if __name__ == '__main__':
    a = ListNode(5)
    a.add_node([1, 2, 3, 4])
    # a.next.next.next.next.next = a.next

    solution = Solution()
    result = solution.detectCycle(a)
    print(result)

# """
# 分析:
# I was wondering aren't we supposed to not use extra space for this problem ?
# Could you please explain your solution. Thanks!
#
# """
