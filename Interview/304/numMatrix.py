class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrixArea = [[-1]*len(matrix[0]) for i in range(len(matrix))]
        cur=0
        for i in range(len(matrix[0])):
            cur+=matrix[0][i]
            self.matrixArea[0][i]=cur
        cur=0
        for j in range(len(matrix)):
            cur+=matrix[j][0]
            self.matrixArea[j][0]=cur
        
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                self.matrixArea[i][j]=self.matrixArea[i-1][j]+self.matrixArea[i][j-1]-self.matrixArea[i-1][j-1]+matrix[i][j]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ret = self.matrixArea[row2][col2]
        if row1 > 0:
            ret-=self.matrixArea[row1-1][col2]
        if col1 > 0:
            ret-=self.matrixArea[row2][col1-1]
        if row1>0 and col1>0:
            ret+=self.matrixArea[row1-1][col1-1]
        return ret
