#include <queue>
#include <vector>

class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        const vector<vector<int>> directions = {{0,1},{1,0},{-1,0},{0,-1},{-1,-1},{-1,1},{1,-1},{1,1}};
        queue<pair<int,int>> q;
        
        if (grid[0][0]!=0) return -1;
        q.emplace(0,0);
        grid[0][0] = 1;
        
        while (q.size()>0){
            const auto [curRow, curCol] = q.front();
            q.pop();
            
            if (curRow==grid.size()-1 && curCol==grid[0].size()-1){
                return grid[grid.size()-1][grid[0].size()-1];
            }
            
            for(const auto & direction: directions){
                int nextRow = direction[0] + curRow;
                int nextCol = direction[1] + curCol;
                if ((nextRow>=0 && nextRow<grid.size()) && 
                    (nextCol>=0 && nextCol<grid[0].size()) &&
                    (grid[nextRow][nextCol]==0)) {
                    grid[nextRow][nextCol]=grid[curRow][curCol]+1;
                    q.emplace(nextRow, nextCol);
                }
            }
        }
        
        return -1;
        
    }
};
