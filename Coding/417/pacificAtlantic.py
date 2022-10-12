import queue
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        reach_pacific = [[False]*len(heights[0]) for i in range(len(heights))]
        reach_atlantic = [[False]*len(heights[0]) for i in range(len(heights))]
        pacific_queue = queue.Queue()
        atlantic_queue = queue.Queue()
        
        for i in range(len(heights[0])):
            reach_pacific[0][i] = True
            reach_atlantic[len(heights)-1][i] = True
            pacific_queue.put([0,i])
            atlantic_queue.put([len(heights)-1,i])
            
        for j in range(len(heights)):
            reach_pacific[j][0] = True
            reach_atlantic[j][len(heights[0])-1] = True
            pacific_queue.put([j,0])
            atlantic_queue.put([j,len(heights[0])-1])
        
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        while pacific_queue.qsize()>0:
            cur = pacific_queue.get()
            for d in directions:
                newPos = [cur[0]+d[0],cur[1]+d[1]]
                if 0 <= newPos[0]< len(heights) and 0 <= newPos[1] < len(heights[0]) and reach_pacific[newPos[0]][newPos[1]]==False and heights[newPos[0]][newPos[1]] >= heights[cur[0]][cur[1]] :
                    reach_pacific[newPos[0]][newPos[1]]=True
                    pacific_queue.put(newPos)
        
        while atlantic_queue.qsize()>0:
            cur = atlantic_queue.get()
            for d in directions:
                newPos = [cur[0]+d[0],cur[1]+d[1]]
                if 0 <= newPos[0]< len(heights) and 0 <= newPos[1] < len(heights[0]) and reach_atlantic[newPos[0]][newPos[1]]==False and heights[newPos[0]][newPos[1]] >= heights[cur[0]][cur[1]] :
                    reach_atlantic[newPos[0]][newPos[1]]=True
                    atlantic_queue.put(newPos)
        ret = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if reach_atlantic[i][j] and reach_pacific[i][j]:
                    ret.append([i,j])
        return ret

