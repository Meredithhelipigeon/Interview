from collections import deque
class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.score = 0
        # 0: empty; 
        # 1: snake; 
        self.grid = [[0] * width for i in range(height)]
        self.body = deque([(0,0)])
        self.grid[0][0] = 1
        self.meatIndex = 0
        self.food = food
        self.directions = {
            "U": [-1,0],
            "D":[1,0],
            "L": [0,-1],
            "R": [0,1]
        }
        

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        curPos = self.body[-1]
        nextPos = [self.directions[direction][0]+curPos[0], self.directions[direction][1]+curPos[1]]
        
        if not (0 <= nextPos[0] < len(self.grid) and 0 <= nextPos[1] < len(self.grid[0])): 
            return -1
        else:
            if self.meatIndex < len(self.food) and self.food[self.meatIndex][0]==nextPos[0] and self.food[self.meatIndex][1]==nextPos[1]:
                self.meatIndex += 1
                self.body.append(nextPos)
                self.score += 1
                self.grid[nextPos[0]][nextPos[1]] = 1
            else:
                tail = self.body.popleft()
                self.grid[tail[0]][tail[1]] = 0
                if self.grid[nextPos[0]][nextPos[1]]==1:
                    return -1
                else:
                    self.body.append(nextPos)
                    self.grid[nextPos[0]][nextPos[1]] = 1
        return self.score
        
# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
