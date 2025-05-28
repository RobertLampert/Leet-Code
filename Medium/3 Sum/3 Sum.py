class Solution(object):   
    def threeSum(self, nums):
        nums.sort()
        returnSet = set()
        for i in range(len(nums)):
            anchor = -nums[i]
            left = 1
            right = len(nums)-1
            while( left != right):
                if nums[left]+nums[right] == anchor and left != i and right != i:
                    curTuple = tuple(sorted((nums[left],nums[right],anchor*-1)))
                    returnSet.add(curTuple)
                    left+=1
                elif nums[left]+nums[right] < anchor:
                    left+=1
                else:
                    right-=1
        answer = list(returnSet)
        return answer

        

solution = Solution()
array = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
print(solution.threeSum(array))