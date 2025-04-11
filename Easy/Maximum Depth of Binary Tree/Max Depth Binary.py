# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.depth = 0

        def depth(root): 
            if not root:
                return 0
            else:
                self.depth +=1
            left = depth(root.left)
            right = depth(root.right)
            self.depth = max(left,right)+1
            return self.depth

        depth(root)
        return self.depth