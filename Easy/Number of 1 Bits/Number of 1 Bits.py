class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        binString = bin(n)
        return binString.count("1")
        

solution = Solution()
print(solution.hammingWeight(128))