class Solution(object):
    def majorityElement(self, nums):
        majority = len(nums)/2
        countDict = {}
        for i in range(len(nums)):
            if countDict.get(nums[i]) != None:
                newCount = countDict.get(nums[i])+1
                countDict.update({nums[i]:newCount})
            else:
                countDict.update({nums[i]:1})
        for key in countDict:
            if countDict.get(key) > majority:
                return key

solution = Solution()
testNums = [1,2,3,1,2,3,1,1,1]
print(solution.majorityElement(testNums))        
