# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        global ret
        ret = []
        
        def dfs(cur):
            global ret
            if cur!=None:
                dfs(cur.left)
                dfs(cur.right)
                ret.append(cur.val)
        dfs(root)
        return ret
