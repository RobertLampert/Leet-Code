# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        def isSameTree(p, q):
            if not p and not q:
                return True
            elif not p or not q:
                return False
            elif p.val == q.val:
                return isSameTree(p.left,q.left) and isSameTree(p.right,q.right)
            else:
                return False
        TreeQ = deque([root])
        result = False
        while TreeQ:
            current = TreeQ.popleft()
            if current.val == subRoot.val:
                if isSameTree(current,subRoot):
                    return True
            if current.left:
                TreeQ.append(current.left) 
            if current.right:
                TreeQ.append(current.right)
        return result
        
