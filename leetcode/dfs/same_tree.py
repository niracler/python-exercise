# """
# 题目：Given two binary trees, write a function to check if they are the same or not.
#
# Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
#
# Example 1:
#
# Input:     1         1
#           / \       / \
#          2   3     2   3
#
#         [1,2,3],   [1,2,3]
#
# Output: true
# Example 2:
#
# Input:     1         1
#           /           \
#          2             2
#
#         [1,2],     [1,null,2]
#
# Output: false
# Example 3:
#
# Input:     1         1
#           / \       / \
#          2   1     1   2
#
#         [1,2,1],   [1,1,2]
#
# Output: false
#
# url:https://leetcode.com/problems/same-tree/
# """
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def preTra(self, p: TreeNode, q: TreeNode):
        if not p and not q:
            return True

        if not p or not q or p.val != q.val:
            return False

        res1 = self.preTra(p.left, q.left)  # 遍历左子树
        res2 = self.preTra(p.right, q.right)  # 遍历右子树

        if not res1 or not res2:
            return False
        else:
            return True

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return self.preTra(p, q)


if __name__ == '__main__':
    p = TreeNode(6)
    p.left = TreeNode(2)
    p.left.left = TreeNode(0)
    p.left.right = TreeNode(4)
    p.left.right.left = TreeNode(3)
    p.left.right.right = TreeNode(5)
    p.right = TreeNode(8)
    p.right.left = TreeNode(7)
    p.right.right = TreeNode(9)

    q = TreeNode(6)
    q.left = TreeNode(2)
    q.left.left = TreeNode(0)
    q.left.right = TreeNode(4)
    q.left.right.left = TreeNode(3)
    q.left.right.right = TreeNode(5)
    q.right = TreeNode(8)
    q.right.left = TreeNode(7)
    q.right.right = TreeNode(99)

    solution = Solution()
    result = solution.isSameTree(p, q)
    print(result)

# """
# 分析:
#
# """
