# """
# 题目：Given a binary search tree, rearrange the tree in in-order so that
# the leftmost node in the tree is now the root of the tree,
# and every node has no left child and only 1 right child.
#
# Example 1:
# Input: [5,3,6,2,4,null,8,1,null,null,null,7,9]
#
#        5
#       / \
#     3    6
#    / \    \
#   2   4    8
#  /        / \
# 1        7   9
#
# Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
#
#  1
#   \
#    2
#     \
#      3
#       \
#        4
#         \
#          5
#           \
#            6
#             \
#              7
#               \
#                8
#                 \
#                  9
#
# url:https://leetcode.com/problems/increasing-order-search-tree/
# """


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        res = TreeNode(-1)
        self.cur = res
        self.inTra(root)

        return res.right

    def inTra(self, root: TreeNode):
        if not root: return

        self.inTra(root.left)  # 遍历左子树
        root.left = None
        self.cur.right = root
        self.cur = root
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
    result = solution.increasingBST(tree)

    print(result)

# """
# 分析:
#
# """
