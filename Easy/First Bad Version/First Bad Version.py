class Solution(object):
    def firstBadVersion(self, n):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(n):
            if isBadVersion(i):
                return i




