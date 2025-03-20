# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        def getHeight(node):
            if not node:
                return 0

            leftHeight = getHeight(node.left)
            rightHeight = getHeight(node.right)

            if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
                return -1

            return 1 + max(leftHeight, rightHeight)

        return getHeight(root) != -1
            