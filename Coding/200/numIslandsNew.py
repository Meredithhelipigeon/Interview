import queue
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False]*len(grid[0]) for i in range(len(grid))]
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        def bfs(i,j):
            q = queue.Queue()
            visited[i][j]=True
            q.put([i,j])

            while q.qsize()>0:
                curPos = q.get()
                for d in directions:
                    nextPos = [curPos[0]+d[0], curPos[1]+d[1]]
                    if 0<=nextPos[0]<len(grid) and 0<=nextPos[1]<len(grid[0]) and grid[nextPos[0]][nextPos[1]]=="1" and (not visited[nextPos[0]][nextPos[1]]):
                        visited[nextPos[0]][nextPos[1]]=True
                        q.put(nextPos)
        
        ret = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (not visited[i][j]) and grid[i][j]=="1":
                    bfs(i,j)
                    ret += 1
        return ret
