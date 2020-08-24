class Matrix:
    
    def matrix(self,rowNum, colNum):
        mtrx = []
        for i in range(rowNum):           
            rowline =[]
            for j in range(colNum):      
                rowline.append(int(input()))
            mtrx.append(rowline) 
        return mtrx
    
    def transpose(self, m):
        dim_row = len(m)
        dim_col = len(m[0])
        trans_M =[[0 for i in range(dim_row)] for j in range(dim_col)]
        for i in range(dim_row):
            for j in range(dim_col):
                trans_M[j][i]= m[i][j]
        return trans_M
    
    def trace(self, m):
        summation = 0
        j=0
        for i in range(len(m)):
            temp = m[i][j]
            summation = temp + summation
            j = j+1
        return summation
