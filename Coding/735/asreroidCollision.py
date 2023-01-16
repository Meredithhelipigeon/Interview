class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        movingRightAster = []
        ret = []
        for asteroid in asteroids:
            if asteroid>0:
                movingRightAster.append(asteroid)
            else:
                ifExplode = False
                while len(movingRightAster)>0:
                    if movingRightAster[-1]>=abs(asteroid):
                        ifExplode = True
                        if movingRightAster[-1]==abs(asteroid):
                            movingRightAster.pop()
                        break
                    else:
                        movingRightAster.pop()
                if not ifExplode:
                    ret.append(asteroid)
        ret.extend(movingRightAster)
        return ret
        
