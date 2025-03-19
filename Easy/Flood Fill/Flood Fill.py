class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        m = len(image)-1
        n = len(image[0])-1
        valModify = image[sr][sc]

        if(image[sr][sc] == color):
            return image

        image[sr][sc] = color
        if(sc-1>=0):
            if(image[sr][sc-1] == valModify):
                self.floodFill(image,sr,sc-1,color)   
        if(sc+1<=n):
            if(image[sr][sc+1] == valModify):
                self.floodFill(image,sr,sc+1,color)
        if(sr-1>=0):
            if(image[sr-1][sc] == valModify):
                self.floodFill(image,sr-1,sc,color)    
        if(sr+1<=m):
            if(image[sr+1][sc] == valModify):
                self.floodFill(image,sr+1,sc,color) 
        return image


solution = Solution()
image = [[1,1,1],[1,1,0],[1,0,1]]
print(solution.floodFill(image,1,1,2))

