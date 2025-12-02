class Solution:
    def spiralOrder(self, matrix):
        n = len(matrix)
        top = 0
        left = 0
        bottom , right = n-1, len(matrix[0])-1
        res = []
        while top<=bottom and left<=right:
            #right
            for i in range(left,right+1):
                res.append(matrix[top][i])
            top+=1
            #bottom
            for i in range(top,bottom+1):
                res.append(matrix[i][right])
            right-=1
            #left
            if (top<=bottom): #what if theres a single row
                for i in range(right, left-1, -1):
                    res.append(matrix[bottom][i])
                bottom-=1
            #top
            if(left<=right):
                for i in range(bottom, top-1, -1):
                    res.append(matrix[i][left])   
                left+=1 
        return res   
     