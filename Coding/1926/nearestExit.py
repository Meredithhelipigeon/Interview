import queue
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        q = queue.Queue()
        q.put((entrance,0))
        visited = [[False for i in range(len(maze[0]))] for j in range(len(maze))]
        visited[entrance[0]][entrance[1]]=True
        directions = [[-1,0],[1,0],[0,1],[0,-1]]
        
        while q.qsize()>0:
            curPos, steps = q.get()
            for d in directions:
                nextPos = [curPos[0]+d[0],curPos[1]+d[1]]
                if 0<=nextPos[0]<len(maze) and 0<=nextPos[1]<len(maze[0]) and visited[nextPos[0]][nextPos[1]]==False and maze[nextPos[0]][nextPos[1]]==".":
                    if nextPos[0]==0 or nextPos[0]==len(maze)-1 or nextPos[1]==0 or nextPos[1]==len(maze[0])-1:
                        return steps + 1
                    else:
                        visited[nextPos[0]][nextPos[1]]=True
                        q.put((nextPos, steps+1))
        return -1
