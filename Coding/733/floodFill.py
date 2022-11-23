import queue
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        direction = [[-1,0],[1,0],[0,1],[0,-1]]
        startColor = image[sr][sc]
        
        q = queue.Queue()
        q.put([sr,sc])
        visited = [[False for i in range(len(image[0]))] for j in range(len(image))]
        visited[sr][sc]=True
        image[sr][sc]=color
        
        while q.qsize() > 0:
            cur = q.get()
            for d in direction:
                nextRow, nextCol = cur[0]+d[0], cur[1]+d[1]
                if 0<=nextRow<len(image) and 0<=nextCol<len(image[0]) and visited[nextRow][nextCol]==False and image[nextRow][nextCol]==startColor:
                    image[nextRow][nextCol] = color
                    q.put([nextRow,nextCol])
                    visited[nextRow][nextCol]=True
        return image
