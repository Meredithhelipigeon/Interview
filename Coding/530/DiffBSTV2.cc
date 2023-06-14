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
private:
    void inorderTraversal(TreeNode* curNode, vector<int> & nums){
        if (curNode==NULL){
            return;
        }
        inorderTraversal(curNode->left, nums);
        nums.push_back(curNode->val);
        inorderTraversal(curNode->right, nums);
    }
public:
    int getMinimumDifference(TreeNode* root) {
        vector<int> nums;
        inorderTraversal(root, nums);
        
        int diff = nums[nums.size()-1] - nums[0];
        for(int i = 1; i < nums.size(); i++){
            diff = min(nums[i]-nums[i-1], diff);
        }
        return diff;
    }
};
