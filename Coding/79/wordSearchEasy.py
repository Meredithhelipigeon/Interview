class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[False for i in range(len(board[0]))] for j in range(len(board))]
        direction = [[0,1],[0,-1],[1,0],[-1,0]]
        
        def dfs(i,curPos):
            if i==len(word):
                return True
            for d in direction:
                nextPos = [curPos[0]+d[0],curPos[1]+d[1]]
                if 0<=nextPos[0]<len(board) and 0<=nextPos[1]<len(board[0]) and visited[nextPos[0]][nextPos[1]]==False and board[nextPos[0]][nextPos[1]]==word[i]:
                    visited[nextPos[0]][nextPos[1]] = True
                    if dfs(i+1,nextPos):
                        return True
                    visited[nextPos[0]][nextPos[1]] = False
            return False
        
        if len(word)==0:
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    visited[i][j]=True
                    if dfs(1,[i,j]):
                        return True
                    visited[i][j]=False
        return False
                        
