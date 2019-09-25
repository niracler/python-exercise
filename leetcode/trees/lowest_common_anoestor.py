# """
# 题目：Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
#
# Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]
#
#
#
#
# Example 1:
#
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.
# Example 2:
#
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2,
# since a node can be a descendant of itself according to the LCA definition.
#
#
# Note:
#
# All of the nodes' values will be unique.
# p and q are different and both values will exist in the BST.
#
# url:https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# """


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.has_p = False
        self.has_q = False

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q: return root  # 假如是空，或找到了，就直接返回root
        left = self.lowestCommonAncestor(root.right, p, q)  # 看看左边有没有
        right = self.lowestCommonAncestor(root.left, p, q)  # 看看右边有没有

        if not right: return left
        if not left: return right
        return root


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
    result = solution.lowestCommonAncestor(tree, tree.left, tree.left.right)  # 2 and 4
    print(result.val)

# """
# 分析:
# 1. 找父亲结点的方法
# 2. 遍历，然后找相同地方
# 3. 又是递归大法，你看看左边有没有，你看看右边有没有，要是都有，那就88
#
# """
