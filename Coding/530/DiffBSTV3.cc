#include <queue>
#include <vector>
#include <limits>
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
    void inorderTraversal(TreeNode* curNode, vector<int> & nums, int & diff){
        if (curNode==NULL){
            return;
        }
        inorderTraversal(curNode->left, nums, diff);
        nums.push_back(curNode->val);
        if (nums.size()>=2) diff = min(nums[nums.size()-1]-nums[nums.size()-2], diff);
        inorderTraversal(curNode->right, nums, diff);
    }
public:
    int getMinimumDifference(TreeNode* root) {
        vector<int> nums;
        int diff = numeric_limits<int>::max();
        inorderTraversal(root, nums, diff);
        
        return diff;
    }
};
