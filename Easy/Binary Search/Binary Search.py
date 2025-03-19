class Solution(object):
    def binarySearch(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        middleIndex = int(len(nums)/2)
        left = 0
        right = len(nums)-1
        
        while(left<=right):
            mid = int((left+right)/2)
            if(nums[mid] == target):
                return mid
            elif(nums[mid]<target):
                left = mid+1
            else:
                right = mid-1
        return -1





solution = Solution()
nums = [-1,0,3,5,9,12]
target = 15
print(solution.binarySearch(nums,target)) 