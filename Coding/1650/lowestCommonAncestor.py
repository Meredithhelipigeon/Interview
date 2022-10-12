# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ret = None
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ret = root
        def find_element(cur):
            if cur==None:
                return False
            
            right = find_element(cur.right)
            left = find_element(cur.left)
            
            if (right and left) or ((right or left) and (cur.val==p.val or cur.val==q.val)):
                    self.ret = cur
            
            if cur.val==p.val or cur.val==q.val or right or left:
                return True
            
        find_element(root)
        return self.ret
