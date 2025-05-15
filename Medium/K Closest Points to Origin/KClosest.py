class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        points.sort(key=lambda x: x[0]**2 + x[1]**2)
        return points[:k]

        
solution = Solution()
k = 1
points = [[1,3],[-2,2]]
print(solution.kClosest(points,k))