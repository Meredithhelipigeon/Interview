class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        ret = 0
        curPos = (0,0)
        curDir = 0
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        uniqueObstacles = set()
        for ob in obstacles:
            uniqueObstacles.add((ob[0],ob[1]))
        
        for command in commands:
            if command==-2:
                curDir = (curDir-1)%4
            elif command==-1:
                curDir = (curDir+1)%4
            elif 1 <= command <= 9:
                for i in range(command):
                    nextPos = (curPos[0]+directions[curDir][0],curPos[1]+directions[curDir][1])
                    if not nextPos in uniqueObstacles:
                        curPos = nextPos
            ret = max(ret, curPos[0]**2 + curPos[1]**2)
        return ret
