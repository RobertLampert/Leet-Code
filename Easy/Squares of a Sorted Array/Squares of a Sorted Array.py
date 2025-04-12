class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arrLength = len(nums)
        finalNums = [0] * arrLength
        i = arrLength - 1
        left = 0
        right = arrLength-1
        while left <= right:
            if nums[left]**2 > nums[right]**2:
                finalNums[i] = nums[left]**2
                i -= 1
                left +=1
            else:
                finalNums[i] = nums[right]**2
                i-=1
                right -= 1
        return finalNums
    
solution = Solution()
nums = [-7,-3,2,3,11]
print(solution.sortedSquares(nums))