class Solution(object):
    def addBinary(self, a, b):
        firstLen = len(a)
        secondLen = len(b)
        loopLength = max(firstLen,secondLen)
        if firstLen-secondLen > 0:
            b = (firstLen-secondLen+1)*"0" + b
            a = "0" + a
        else:
            a = (secondLen-firstLen+1)*"0" + a
            b = "0" + b
        rem = 0
        returnBinaryString = ""
        for i in range(loopLength,-1,-1):
            sum = int(a[i]) + int(b[i]) + rem
            if sum == 3:
                rem =1
                returnBinaryString = "1" + returnBinaryString
            elif sum == 2:
                rem=1
                returnBinaryString = "0" + returnBinaryString
            else:
                rem = 0
                returnBinaryString = str(sum) + returnBinaryString
        if returnBinaryString[0] == "0":
            returnBinaryString = returnBinaryString[1:]
        return returnBinaryString
    


testString1 = "1111"
testString2 = "1111"
solution = Solution()
print(solution.addBinary(testString1,testString2))