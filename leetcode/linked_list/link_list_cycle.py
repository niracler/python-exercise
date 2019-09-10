# """
# 题目：
#
# url:https://leetcode.com/problems/linked-list-cycle/
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
    def hasCycle(self, head: ListNode) -> bool:

        if not head:
            return False

        fast = head.next
        slow = head

        while fast and fast.next and slow:
            if fast == slow:
                return True
            fast = fast.next.next
            slow = slow.next

        return False


if __name__ == '__main__':
    a = ListNode(5)
    a.add_node([1, 2, 3, 4])
    a.next.next.next.next.next = a.next

    solution = Solution()
    result = solution.hasCycle(a)
    print(result)

# """
# 分析:快慢指针两倍速跑步法
#
# """
