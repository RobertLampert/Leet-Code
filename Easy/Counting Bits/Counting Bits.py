class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            numOneArr = [0]
            return numOneArr
        
        numOneArr = [0,1]
        for i in range(2,n+1):
            if i % 2 == 0:
                numOneArr.append(numOneArr[int(i/2)])
            else:
                numOneArr.append(numOneArr[i-1]+1)
        return numOneArr
