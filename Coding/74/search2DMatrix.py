class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        start, end = 0, m*n-1

        while start <= end:
            mid = (start+end) // 2
            mid_value = matrix[mid//n][mid%n]
            if mid_value == target:
                return True
            elif mid_value < target:
                start = mid+1
            else:
                end = mid-1
        
        return False
