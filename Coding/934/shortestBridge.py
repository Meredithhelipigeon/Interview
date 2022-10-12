import queue
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        find=False
        
        # Step 1. find one point in one island
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    start = [i,j]
                    find=True
                    break
            if find:
                break
        
        potentialStarts = queue.Queue()
        visited = [[False]*len(grid[0]) for i in range(len(grid))]
        q = queue.Queue()
        q.put(start)
        potentialStarts.put([start,0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        
        # Step 2. Mark all of the island visited 
        while q.qsize()>0:
            cur = q.get()
            visited[cur[0]][cur[1]]=True
            for d in directions:
                newPos = [cur[0]+d[0],cur[1]+d[1]]
                if 0<=newPos[0]<len(grid) and 0<=newPos[1]<len(grid[0]) and grid[newPos[0]][newPos[1]]==1 and not visited[newPos[0]][newPos[1]]:
                    q.put(newPos)
                    potentialStarts.put([newPos,0])
                    
        
        # Step 3. Use BFS to find the shortest path from Island 1 to Island 2
        while potentialStarts.qsize()>0:
            cur, curDistance = potentialStarts.get()
            visited[cur[0]][cur[1]]=True
            for d in directions:
                newPos = [cur[0]+d[0],cur[1]+d[1]]
                if 0<=newPos[0]<len(grid) and 0<=newPos[1]<len(grid[0]) and not visited[newPos[0]][newPos[1]]:
                    if grid[newPos[0]][newPos[1]]==1:
                        return curDistance
                    potentialStarts.put([newPos,curDistance+1])
        
        return -1        
