import queue

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        neighbours = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,-1],[-1,1]]
        visited = [[False]*len(grid[0]) for i in range(len(grid))]
        q = queue.Queue()
        
        if grid[0][0]!=0:
            return -1
        q.put((0,0,1))
        visited[0][0]=True
        
        while q.qsize()>0:
            curRow, curCol, steps = q.get()
            if curRow==len(grid)-1 and curCol==len(grid[0])-1:
                return steps
            for [addRow, addCol] in neighbours:
                nextRow, nextCol = addRow+curRow, addCol+curCol
                if 0<=nextRow<len(grid) and 0<=nextCol<len(grid[0]) and not visited[nextRow][nextCol] and grid[nextRow][nextCol]==0:
                    visited[nextRow][nextCol] = True
                    q.put((nextRow,nextCol,steps+1))
        return -1
