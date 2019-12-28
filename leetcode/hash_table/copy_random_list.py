# """
# 题目：A linked list is given such that each node contains an
# additional random pointer which could point to any node in the list or null.
#
# Return a deep copy of the list.
#
# The Linked List is represented in the input/output as a list of n nodes.
# Each node is represented as a pair of [val, random_index] where:
#
# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) where random pointer points to,
# or null if it does not point to any node.
#
#
# Example 1:
#
# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
#
# Example 2:
#
# Input: head = [[1,1],[2,1]]
# Output: [[1,1],[2,1]]
# Example 3:
#
#
#
# Input: head = [[3,null],[3,0],[3,null]]
# Output: [[3,null],[3,0],[3,null]]
# Example 4:
#
# Input: head = []
# Output: []
# Explanation: Given linked list is empty (null pointer), so return null.
#
# url:https://leetcode.com/problems/copy-list-with-random-pointer/
# """


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def print_node(self):
        cur = self
        while cur:
            if cur.random:
                print("val = " + str(cur.val) + ", r_val = " + str(cur.random.val))
            else:
                print("val = " + str(cur.val) + ", r_val = " + str(cur.random))
            cur = cur.next


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        res = Node(head.val)
        cur_res = res
        cur = head.next
        res_map = {
            head: res
        }

        # 第一次遍历
        while cur:
            cur_res.next = Node(cur.val)
            res_map[cur] = cur_res.next
            cur = cur.next
            cur_res = cur_res.next

        # 第二次遍历
        cur_res = res
        cur = head
        while cur:
            if cur.random:
                cur_res.random = res_map[cur.random]

            cur = cur.next
            cur_res = cur_res.next

        return res


if __name__ == '__main__':
    # [[7, null], [13, 0], [11, 4], [10, 2], [1, 0]]
    root = Node(7, random=None)
    root.next = Node(13, random=root)
    root.next.next = Node(11)
    root.next.next.next = Node(10, random=root.next.next)
    root.next.next.next.next = Node(1, random=root)
    root.next.next.random = root.next.next.next.next
    root.print_node()

    solution = Solution()
    result = solution.copyRandomList(root)
    result.print_node()

# """
# 分析:这道题难就难在如何获取对应的随机的节点。
# 哦哦，好像也可以一次遍历就完成， 不过一次遍历的时候， 需要将那些 random 的节点也生成出来
#
# """
