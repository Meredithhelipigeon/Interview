class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles_set = set()
        for o in obstacles:
            obstacles_set.add((o[0],o[1]))
        
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        curDirection = 0
        curPos = (0,0)
        ret = 0
        start = True
        
        for command in commands:
            if command == -1:
                curDirection = (curDirection + 1) % 4
            elif command == -2:
                curDirection = (curDirection - 1) % 4
            else:
                nextPos = curPos
                while (nextPos not in obstacles_set and command >= 0) or (start and nextPos == (0,0)):
                    command -= 1
                    curPos = nextPos
                    nextPos = (curPos[0]+directions[curDirection][0], curPos[1]+directions[curDirection][1])
                    start = False
                ret = max(ret, curPos[0]**2 + curPos[1]**2)
        return ret
            
