from collections import deque

class Solution(object):
    def isSymmetric(self, root):
        queue = deque([(root, root)])

        while queue:
            node1, node2 = queue.popleft()
            if not node1 and not node2:
                continue
            if not node1 or not node2 or node1.val != node2.val:
                return False
            queue.append((node1.left, node2.right))
            queue.append((node1.right, node2.left))

        return True