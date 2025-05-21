class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        mySet = set()
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if len({i, j, k}) == 3 and nums[i] + nums[j] + nums[k] == 0:
                        myTuple = (nums[i],nums[j],nums[k])
                        sortedTuple = tuple(sorted(myTuple))
                        mySet.add(sortedTuple)
        return list(mySet)
solution = Solution()
array = [-1,0,1,2,-1,-4]
print(solution.threeSum(array))