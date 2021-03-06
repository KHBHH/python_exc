class Matrix:
    
    ####function to create matrix of size rowNum x colNum
    #the entries of the matrix should be an input from the user
    def matrix(self,rowNum, colNum):
        mtrx = []
        for i in range(rowNum):           
            rowline =[]
            for j in range(colNum):      
                rowline.append(int(input()))
            mtrx.append(rowline) 
        return mtrx
    
    ####function to multiply matrix by scalar
    def scal_mult(self,matrix, scalar):
        result = matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                result[i][j] = scalar * matrix[i][j]
        return result
    
    ####multiplication & addition of 2 matrices
    def matrix_arithmetic(self,A,B, operator):
        rows_A = len(A)
        columns_A = len(A[0])
        rows_B = len(B)
        columns_B = len(B[0])
        
        if operator == '*':
            if (columns_A != rows_B): #check first if multiplication is possible
                raise ArithmeticError('Invalid dimensions, can not do multiplication')
            else:
                result = [[0 for i in range(columns_B)] for j in range(rows_A)]
                for i in range(rows_A):
                    for j in range(columns_B):
                        temp = 0
                        for k in range(columns_A):
                            temp = temp + A[i][k] * B[k][j]
                        result[i][j] = temp
            return result
        
        elif operator == '+':
            if (rows_A != rows_B or columns_A != columns_B):
                raise ArithmeticError('matrices do not have equal dimension, can not do addition')
            else:
                result = [[0 for i in range(columns_A)] for j in range(rows_A)]
                for i in range(rows_A):
                    for j in range(columns_A):
                        result[i][j] = A[i][j] + B[i][j]
            return result
    
    ####function to find the transpose of matrix m
    def transpose(self, m):
        dim_row = len(m)
        dim_col = len(m[0])
        trans_M =[[0 for i in range(dim_row)] for j in range(dim_col)]
        for i in range(dim_row):
            for j in range(dim_col):
                trans_M[j][i]= m[i][j]
        return trans_M
    
    ####function to get the sum of diagonals of matrix m
    def trace(self, m):
        summation = 0
        j=0
        for i in range(len(m)):
            temp = m[i][j]
            summation = temp + summation
            j = j+1
        return summation
    
    ####function to find the determinant of matrix m
    
    
    
    ###function to get the inverse of matrix m
