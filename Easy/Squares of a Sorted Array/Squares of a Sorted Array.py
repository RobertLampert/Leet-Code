class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            nums[i] = nums[i] **2
        nums.sort()
        return nums
solution = Solution()
nums = [-4,-1,0,3,10]
print(solution.sortedSquares(nums))