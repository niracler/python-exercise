# """
# 题目： Given a binary tree, return the postorder traversal of its nodes' values.
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
# Output: [3,2,1]
# Follow up: Recursive solution is trivial, could you do it iteratively?
#
# url:https://leetcode.com/problems/binary-tree-postorder-traversal/
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

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        self.posTra(root)
        return self.res

    def posTra(self, root: TreeNode):
        if not root: return

        self.posTra(root.left)  # 遍历左子树
        self.posTra(root.right)  # 遍历右子树
        self.res.append(root.val)


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
    result = solution.posTra(tree)
    print(result)

# """
# 分析:
#
# """
