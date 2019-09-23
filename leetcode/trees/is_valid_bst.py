# """
# 题目：Given a binary tree, determine if it is a valid binary search tree (BST).
#
# Assume a BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
#
#
# Example 1:
#
#     2
#    / \
#   1   3
#
# Input: [2,1,3]
# Output: true
# Example 2:
#
#     5
#    / \
#   1   4
#      / \
#     3   6
#
# Input: [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
#
# """


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        不行，这道题是有所谓的上限和下限的
        :param root:
        :return:
        """
        return self.BSTcheck(float('-inf'), float('inf'), root)

    def BSTcheck(self, minx, maxx, node):
        if node:
            return minx < node.val < maxx and self.BSTcheck(minx, node.val, node.left) and self.BSTcheck(node.val, maxx,
                                                                                               node.right)
        else:
            return True


if __name__ == '__main__':
    tree = TreeNode(1)
    tree.left = TreeNode(1)
    # tree.right = TreeNode(3)
    # tree.right.left = TreeNode(15)
    # tree.right.right = TreeNode(7)

    solution = Solution()
    result = solution.isValidBST(tree)
    print(result)

# """
# 分析:
# 1. 中序遍历，遍历途中是单调递增的
# 2. 递归确认,返回最大值以及最小值
# """
