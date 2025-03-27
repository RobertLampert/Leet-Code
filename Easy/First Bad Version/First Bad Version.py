class Solution(object):
    def firstBadVersion(self, n):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = n
        foundBadVersion = -1
        while left<=right:
            mid = int((left+right)/2)
            if isBadVersion(mid):
                found = mid
                right = mid-1
            else:
                left = mid + 1
        return found
        



