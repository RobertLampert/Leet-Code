class Solution(object):
    def climbStairs(self, n):
        solution = [1,2]
        if n < 3:
            return solution[n-1]
        else:
            for i in range(2,n):
                solution.append(solution[i-1]+solution[i-2])
        return solution[n-1]



#solution = Solution()
#print(solution.climbStairs(10))