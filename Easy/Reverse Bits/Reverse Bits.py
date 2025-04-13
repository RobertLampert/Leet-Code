class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        binNum = bin(n)[2:]
        binaryLength = len(bin(n)[2:])
        if(binaryLength < 32):
            for i in range(32-binaryLength):
                binNum = '0' + binNum
        print(binNum)
        binNum = binNum[::-1]
        finalNum = int(binNum,2)
        return finalNum
        
solution = Solution()
binNum = 43261596
print(solution.reverseBits(binNum))