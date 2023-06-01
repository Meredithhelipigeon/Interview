#include <queue>
#include <vector>

class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        vector<vector<int>> directions = {{0,1},{1,0},{-1,0},{0,-1},{-1,-1},{-1,1},{1,-1},{1,1}};
        queue<pair<int,int>> q;
        if (grid[0][0]!=0) return -1;
        q.push(make_pair(0,0));
        grid[0][0] = 1;
        
        while (q.size()>0){
            pair<int, int> curPos = q.front();
            q.pop();
            if (curPos.first==grid.size()-1 && curPos.second==grid[0].size()-1){
                return grid[grid.size()-1][grid[0].size()-1];
            }
            for(int i = 0; i < directions.size(); i++){
                pair<int, int> nextPos;
                nextPos.first = directions[i][0] + curPos.first;
                nextPos.second = directions[i][1] + curPos.second;
                if ((nextPos.first>=0 && nextPos.first<grid.size()) && 
                    (nextPos.second>=0 && nextPos.second<grid[0].size()) &&
                    (grid[nextPos.first][nextPos.second]==0)) {
                    grid[nextPos.first][nextPos.second]=grid[curPos.first][curPos.second]+1;
                    q.push(nextPos);
                }
            }
        }
        return -1;
        
    }
};
