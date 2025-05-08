class Solution(object):
    def modBinarySearch(self, arr, target):
        left, right = 0, len(arr)
        
        while left < right:
            mid = (left + right) // 2
            if arr[mid][0] < target:
                left = mid + 1
            else:
                right = mid
                
        return left

    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        insertInd = self.modBinarySearch(intervals,newInterval[0]) #find the insertion index
        intervals.insert(insertInd,newInterval)
        left = intervals[insertInd][0]
        right = intervals[insertInd][1]
        if insertInd-1>=0 and intervals[insertInd-1][1] >= left: #merge left
            intervals[insertInd][0] = min(left,intervals[insertInd-1][0])
            intervals[insertInd][1] = max(right,intervals[insertInd-1][1])
            intervals.pop(insertInd-1)
            insertInd -=1
        rightP = insertInd+1 #out of bounds check
        left = intervals[insertInd][0] #reset values
        right = intervals[insertInd][1]
        while(rightP <= len(intervals)-1 and intervals[rightP][0] <= intervals[insertInd][1]): #merge right
            intervals[insertInd][0] = min(left,intervals[insertInd+1][0])
            intervals[insertInd][1] = max(right,intervals[insertInd+1][1])
            intervals.pop(insertInd+1)
        return intervals

solution = Solution()
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
print(solution.insert(intervals,newInterval))
