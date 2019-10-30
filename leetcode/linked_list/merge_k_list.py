# """
# 题目：Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
#
# Example:
#
# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6
#
# url:https://leetcode.com/problems/merge-k-sorted-lists/
# """
import operator
from typing import List


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
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        cur = res = ListNode(1)  # 到时候就返回这个吧
        lists = [i for i in lists if i]  # 清理一下空值
        node_list = []

        # 全拿出来
        for i in lists:
            while i:
                node_list.append(i)
                i = i.next

        node_list.sort(key=operator.attrgetter('val'))

        # 全连起来
        for i in node_list:
            cur.next = i
            cur = cur.next

        # print(list(map(lambda x: x.val, node_list)))

        return res.next


if __name__ == '__main__':
    a = ListNode(1)
    a.add_node([4, 5])
    b = ListNode(1)
    b.add_node([3, 4])
    c = ListNode(2)
    c.add_node([6])

    solution = Solution()
    result = solution.mergeKLists([a, b, c])
    result.print_node()

# """
# 分析:这样吧，全拿出来，再排序
#
# """
