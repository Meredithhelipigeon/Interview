class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_hashMap = [[0]*9 for i in range(9)]
        col_hashMap = [[0]*9 for i in range(9)]
        cell_hashMap = [[0]*9 for i in range(9)]
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]!= ".":
                    cur = int(board[i][j]) - 1
                    if row_hashMap[i][cur] == 0 and col_hashMap[j][cur] == 0 and cell_hashMap[(i//3)*3+j//3][cur]==0:
                        row_hashMap[i][cur] = 1
                        col_hashMap[j][cur] = 1
                        cell_hashMap[(i//3)*3+j//3][cur] = 1
                    else:
                        return False
        return True
