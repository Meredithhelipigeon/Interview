import queue
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.visited = [[False]*len(grid[0]) for i in range(len(grid))]
        directions = [[-1,0], [0,1],[1,0],[0,-1]]
        
        def bfs(self,cur):
            q = queue.Queue()
            q.put(cur)
            self.visited[cur[0]][cur[1]]= True
            
            while q.qsize()>0:
                curPos = q.get()
                for d in directions:
                    newPos = [curPos[0]+d[0],curPos[1]+d[1]]
                    if 0 <=newPos[0]<len(grid) and 0<=newPos[1]< len(grid[0]) and self.visited[newPos[0]][newPos[1]]==False and grid[newPos[0]][newPos[1]]=="1":
                        self.visited[newPos[0]][newPos[1]]=True
                        q.put(newPos)
        
        ret = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1" and self.visited[i][j]==False:
                    bfs(self,[i,j])
                    ret +=1
        return ret
                
                        
