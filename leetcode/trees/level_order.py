# """
# 题目：Binary Tree Level Order Traversal
#   Go to Discuss
# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
#
# """


# Definition for a binary tree node.
import collections
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        二叉树的层序遍历
        :param root:
        :return:
        """
        if root == None:
            return []

        queue = [(root, 0)]
        res = collections.defaultdict(list)

        while queue:
            root, deep = queue.pop(0)
            res[deep].append(root.val)

            if root.left:
                queue.append((root.left, deep + 1))
            if root.right:
                queue.append((root.right, deep + 1))

        return [res[k] for k in res]


if __name__ == '__main__':
    tree = TreeNode(3)
    tree.left = TreeNode(9)
    tree.right = TreeNode(20)
    tree.right.left = TreeNode(15)
    tree.right.right = TreeNode(7)

    solution = Solution()
    result = solution.levelOrder(tree)
    print(result)

# """
# 分析:
#
# """
