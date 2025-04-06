class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        numOneArr = []
        for i in range(n+1):
            binNum = bin(i)
            numOnes = binNum.count("1")
            numOneArr.append(numOnes)
        return numOneArr

solution = Solution()
print(solution.countBits(5))
