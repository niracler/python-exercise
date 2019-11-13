# """
# 题目：Given a binary tree and a sum, determine if the tree has a root-to-leaf path
# such that adding up all the values along the path equals the given sum.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given the below binary tree and sum = 22,
#
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \      \
# 7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
#
# url:https://leetcode.com/problems/path-sum/
# """


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root: return False
        if not root.right and not root.left and sum == root.val:
            return True

        res1 = res2 = False
        if root.left:
            res1 = self.hasPathSum(root.left, sum - root.val)  # 帮我看看左边有没有
        if root.right:
            res2 = self.hasPathSum(root.right, sum - root.val)  # 帮我看看右边有没有

        if res1 or res2:
            return True
        else:
            return False


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

    solution = Solution()
    result = solution.hasPathSum(p, 8)
    print(result)

# """
# 分析:
#
# """
