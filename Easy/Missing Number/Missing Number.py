class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet = set(nums)
        n = 0
        for element in numSet:
            if element == n:
                n+= 1
                continue
            else:
                return n
        return n

solution = Solution()
nums = [0,1]
print(solution.missingNumber(nums))