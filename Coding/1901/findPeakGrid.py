class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:        
        def findPeakSplit(start,end):
            mid = (start+end)//2
            curMax = mat[0][mid]
            curMaxPos = [0,mid]
            for i in range(0,len(mat)):
                for j in range(max(start,mid-1),min(end+1,mid+2)):
                    if mat[i][j]>curMax:
                        curMax = mat[i][j]
                        curMaxPos = [i,j]
            if curMaxPos[1] == mid or end-start < 3:
                return curMaxPos
            elif curMaxPos[1] > mid:
                return findPeakSplit(mid,end)
            else:
                return findPeakSplit(start,mid)
            
        return findPeakSplit(0,len(mat[0])-1)
