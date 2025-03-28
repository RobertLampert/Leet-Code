class Solution(object):
    def longestPalindrome(self, s):
        numEvens = 0
        oddEvenPairs = 0
        finalCount = 0
        oddRemain = False
        freqDict = {}
        for char in s:
            if char not in freqDict.keys():
                val = s.count(char)
                freqDict.update({char:val})
                if val%2 ==0:
                    numEvens +=val/2
                else:
                    oddEvenPairs += int(val/2)
                    oddRemain = True
        if oddRemain:
            finalCount = numEvens*2+oddEvenPairs*2+1
        else:
            finalCount = numEvens*2+oddEvenPairs*2
        return int(finalCount)

solution = Solution()
ex1 = "abccccdd"
ex2 = "a"
ex3 = "ccc"

print(solution.longestPalindrome(ex1))
print(solution.longestPalindrome(ex2))
print(solution.longestPalindrome(ex3))