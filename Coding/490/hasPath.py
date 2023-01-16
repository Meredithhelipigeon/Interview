import queue
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        visited = [[False]*len(maze[0]) for i in range(len(maze))]
        q = queue.Queue()
        q.put(start)
        visited[start[0]][start[1]]=True
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        
        while q.qsize()>0:
            curPos = q.get()
            for d in directions:
                nextPos = [curPos[0],curPos[1]]
                while 0<=nextPos[0]+d[0]<len(maze) and 0<=nextPos[1]+d[1]<len(maze[0]) and (maze[nextPos[0]+d[0]][nextPos[1]+d[1]]==0):
                    nextPos = [nextPos[0]+d[0],nextPos[1]+d[1]]
                if not visited[nextPos[0]][nextPos[1]]:
                    q.put(nextPos)
                    visited[nextPos[0]][nextPos[1]] = True
                    if nextPos==destination:
                        return True
        return False
