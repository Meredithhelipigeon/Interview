import queue
class Solution:
    # Solution 1: BFS bounded by maxMove;
    # Time efficiency: O(4**a) [let a denote maxMove] It is not bounded by m or n since we don't record visited
    # Space complexity: O(4**a) every level
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        curMove = 0
        curQueue = queue.Queue()
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        ret = 0
        curQueue.put([startRow,startColumn])
        
        while (curMove < maxMove and curQueue.qsize()>0):
            nextQueue = queue.Queue()
            while curQueue.qsize()>0:
                curPos = curQueue.get()
                for d in directions:
                    nextPos = [curPos[0]+d[0],curPos[1]+d[1]]
                    if 0<=nextPos[0]<m and 0<=nextPos[1]<n:
                        nextQueue.put(nextPos)
                    else:
                        ret+=1
                        if ret >= 10**9+7:
                            ret %= 10**9+7
            curMove+=1
            curQueue=nextQueue
        return ret

    # Solution 2: (Optimization for Solution 1) Use a dictionary to limit the number of current pathPos.
    # The reason why the space efficiency and time effiency are so high is that the current recorded path
    # are not bouned by the board(m*n). However, there are only at most m*n positions => Use a dict to optimize.
    # Time efficiency: O(maxMove*m*n)
    # Space efficiency: O(m*n)
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        curMove = 0
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        ret = 0
        curPos_to_numbers = {}
        curPos_to_numbers[(startRow,startColumn)]=1
        
        while (curMove < maxMove and len(curPos_to_numbers)>0):
            nextPos_to_numbers = {}
            for curPos in curPos_to_numbers:
                for d in directions:
                    nextPos = (curPos[0]+d[0],curPos[1]+d[1])
                    curPathNum=curPos_to_numbers[curPos]
                    if 0<=nextPos[0]<m and 0<=nextPos[1]<n:
                        if nextPos in nextPos_to_numbers:
                            nextPos_to_numbers[nextPos]+=curPathNum
                        else:
                            nextPos_to_numbers[nextPos]=curPathNum
                    else:
                        ret+=curPathNum
                        if ret >= 10**9+7:
                            ret %= 10**9+7
            curMove+=1
            curPos_to_numbers=nextPos_to_numbers
        return ret
    
