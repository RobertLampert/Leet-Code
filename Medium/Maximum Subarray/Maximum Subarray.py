class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSol = 0
        currSol = 0
        for num in nums:
            currSol+=num
            if currSol > maxSol:
                maxSol = currSol
            if currSol < 0:
                currSol = 0
        if maxSol == 0:
            return max(nums)
        else:
            return maxSol
solution = Solution()
nums = [1,-3,2,0,-1,0,-2,-3,1,2,-3,2]
print(solution.maxSubArray(nums))