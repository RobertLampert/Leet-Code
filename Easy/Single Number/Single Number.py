class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        countDictionary = {}
        for index in nums:
            if countDictionary.get(index):
                countDictionary.pop(index)
            else:
                countDictionary.update({index:1})
        first_key = next(iter(countDictionary.keys()))
        return first_key
        

solution = Solution()
nums = [4,1,2,1,2]
print(solution.singleNumber(nums))