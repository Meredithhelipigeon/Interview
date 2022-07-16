# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Time Complexity: O(n^2); works well when the tree is balanced
# Space Complexity: O(n)
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def recurseTree(po,io):
            if len(po)==0:
                return None
            mid = po[0]
            midIo = io.index(mid)
            leftTree=recurseTree(po[1:midIo+1],io[:midIo])
            rightTree=recurseTree(po[midIo+1:],io[midIo+1:])
            return TreeNode(mid,leftTree,rightTree)
        
        root = recurseTree(preorder,inorder)
        return root

# The worst thing about previous solution is that we have to calculate the position of the midpoint
# for inorder. The optimization here helps to use constant time to know the position.
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution2:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        ioIndexToPosition = {}
        for i in range(len(inorder)):
            ioIndexToPosition[inorder[i]]=i
        def recurseTree(po,io):
            if len(po)==0:
                return None
            mid = po[0]
            midIo = ioIndexToPosition[mid]-ioIndexToPosition[io[0]]
            leftTree=recurseTree(po[1:midIo+1],io[:midIo])
            rightTree=recurseTree(po[midIo+1:],io[midIo+1:])
            return TreeNode(mid,leftTree,rightTree)
        
        root = recurseTree(preorder,inorder)
        return root
