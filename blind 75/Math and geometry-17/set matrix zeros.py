class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # setting markers for first row and first col 
        firstrow = False
        firstcol = False
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    if i==0:
                        firstrow = True
                    if j==0:
                        firstcol = True
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        # inner matrix 
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if (matrix[i][0]==0 or matrix[0][j]==0):
                    matrix[i][j] = 0
        # first row first col checks
        if(firstrow):
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        if (firstcol):
            for i in range(len(matrix)):
                matrix[i][0] = 0

        