class Matrix:
    
    #creating matrix of size rowNum * colNum
    def matrix(self,rowNum, colNum):
        mtrx = []
        for i in range(rowNum):           
            rowline =[]
            for j in range(colNum):      
                rowline.append(int(input()))
            mtrx.append(rowline) 
        return mtrx
    
    #multiplying matrix by scalar
    def scal_mult(self,matrix, scalar):
        result = matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                result[i][j] = scalar * matrix[i][j]
        return result
    
    #transpose matrix m
    def transpose(self, m):
        dim_row = len(m)
        dim_col = len(m[0])
        trans_M =[[0 for i in range(dim_row)] for j in range(dim_col)]
        for i in range(dim_row):
            for j in range(dim_col):
                trans_M[j][i]= m[i][j]
        return trans_M
    
    #getting the sum of the diagonal of the matrix m
    def trace(self, m):
        summation = 0
        j=0
        for i in range(len(m)):
            temp = m[i][j]
            summation = temp + summation
            j = j+1
        return summation
