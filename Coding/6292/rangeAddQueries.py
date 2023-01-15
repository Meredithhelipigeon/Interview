## Solution 1: brute force
## Time Complexity: O(n*n*rowLen*colLen)
class Solution1:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        matrix = [[0]*n for i in range(n)]
        
        for query in queries:
            row1, col1, row2, col2 = query
            for i in range(row1, row2+1):
                for j in range(col1, col2+1):
                    matrix[i][j] += 1
        return matrix

## Solution 2: prefix sum
## Time Complexity: O(n^2)
class Solution2:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        matrix = [[0]*n for i in range(n)]
        
        for row1, col1, row2, col2 in queries:
            matrix[row1][col1]+=1
            if col2+1 < n: matrix[row1][col2+1]-=1
            if row2+1 < n: matrix[row2+1][col1]-=1
            if col2+1<n and row2+1<n: matrix[row2+1][col2+1]+=1
        
        for i in range(1, n):
            for j in range(n):
                matrix[i][j]+=matrix[i-1][j]
        for i in range(n):
            for j in range(1,n):
                matrix[i][j]+=matrix[i][j-1]
        
        return matrix
