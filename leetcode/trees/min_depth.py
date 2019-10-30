# """
# 题目：Given a binary tree, find its maximum depth.
#
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given binary tree [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its depth = 2
# url:https://leetcode.com/problems/minimum-depth-of-binary-tree
#
# """
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.deep = 0


class Solution:

    def minDepth(self, root: TreeNode) -> int:
        """
        返回一棵树的深度
        :param root:
        :return:
        """
        myque = collections.deque()

        if root == None:
            return 0

        root.deep = 1
        myque.append(root)

        while myque:
            item = myque.popleft()
            if item.left:
                item.left.deep = item.deep + 1
                myque.append(item.left)
            if item.right:
                item.right.deep = item.deep + 1
                myque.append(item.right)
            if not item.left and not item.right:
                return item.deep


if __name__ == '__main__':
    tree = TreeNode(3)
    tree.right = TreeNode(9)
    # tree.right = TreeNode(20)
    # tree.right.left = TreeNode(15)
    # tree.right.right = TreeNode(7)

    solution = Solution()
    result = solution.minDepth(tree)
    print(result)

# """
# 分析:
#
# """
