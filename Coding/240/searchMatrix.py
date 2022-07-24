class Solution(object):
    # Time efficiency: O(n*m), Space Complexity: O(1)
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        cur = 0
        
        for i in range(len(matrix)):
            increase = True
            if cur < 0:
                return False
            cur = min(len(matrix[0])-1,cur)
            
            if matrix[i][cur] > target:
                increase = False
            
            while 0 <= cur < len(matrix[0]):
                if matrix[i][cur]==target:
                    return True
                if increase:
                    if matrix[i][cur] > target:
                        break
                    else:
                        cur+=1
                else:
                    if matrix[i][cur] < target:
                        break
                    else:
                        cur-=1
        return False

    # Time efficiency: O(m+n), Space Complexity: O(1)
    # When we try to find the target, first observe the relationship between each point.
    def searchMatrix2(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        cur = [0,len(matrix[0])-1]
        
        while cur[0] < len(matrix) and cur[1] >= 0:
            if matrix[cur[0]][cur[1]]==target:
                return True
            elif matrix[cur[0]][cur[1]]>target:
                cur[1]-=1
            else:
                cur[0]+=1
        return False
