# """
# 题目：Given a binary tree, return the inorder traversal of its nodes' values.
#
# Example:
#
# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# Output: [1,3,2]
# Follow up: Recursive solution is trivial, could you do it iteratively?
#
# url:https://leetcode.com/problems/binary-tree-inorder-traversal
# """

from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.res = []

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.inTra(root)
        return self.res

    def inTra(self, root: TreeNode):
        if not root: return

        self.inTra(root.left)  # 遍历左子树
        self.res.append(root.val)
        self.inTra(root.right)  # 遍历右子树


if __name__ == '__main__':
    tree = TreeNode(6)
    tree.left = TreeNode(2)
    tree.left.left = TreeNode(0)
    tree.left.right = TreeNode(4)
    tree.left.right.left = TreeNode(3)
    tree.left.right.right = TreeNode(5)
    tree.right = TreeNode(8)
    tree.right.left = TreeNode(7)
    tree.right.right = TreeNode(9)

    solution = Solution()
    result = solution.inorderTraversal(tree)
    print(result)

# """
# 分析:
#
# """
