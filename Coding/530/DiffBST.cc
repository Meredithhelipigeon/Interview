#include <queue>
#include <vector>
using namespace std;

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int getMinimumDifference(TreeNode* root) {
        queue<TreeNode*> q;
        vector<int> nums;
        q.push(root);
            
        while (q.size()>0){
            TreeNode * curNode = q.front();
            q.pop();
            nums.push_back(curNode->val);
            if (curNode->left) q.push(curNode->left);
            if (curNode->right) q.push(curNode->right);
        }
        sort(nums.begin(), nums.end());
        
        int diff = nums[nums.size()-1] - nums[0];
        for(int i = 1; i < nums.size(); i++){
            diff = min(nums[i]-nums[i-1], diff);
        }
        return diff;
    }
};
