# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        stack = [root]
        
        while len(stack)>0:
            curNode = stack.pop()
            if curNode!=None:
                ret.append(curNode.val)
                stack.append(curNode.right)
                stack.append(curNode.left)
    
        return ret
