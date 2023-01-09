# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        
        def searchInTree(curNode):
            if curNode==None:
                return
            else:
                ret.append(curNode.val)
                searchInTree(curNode.left)
                searchInTree(curNode.right)
        searchInTree(root)
        return ret
