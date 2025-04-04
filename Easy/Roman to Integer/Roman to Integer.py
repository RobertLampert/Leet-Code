class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romanIntDict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        sum = 0
        if len(s) == 1:
            return romanIntDict.get(s[0])
        for i in range(len(s)-1):
            if romanIntDict.get(s[i]) < romanIntDict.get(s[i+1]):
                sum -= romanIntDict.get(s[i])
            else:
                sum += romanIntDict.get(s[i])
        sum+=romanIntDict.get(s[len(s)-1])
        return sum


solution = Solution()
print(solution.romanToInt("IV"))