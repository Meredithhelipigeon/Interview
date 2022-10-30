# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        self.heightsToNums = []
        self.indexToTreeNode = {}
        self.indexToHeight = {}
        
        def dfs(self, cur, h):
            if cur!=None:
                if h >= len(self.heightsToNums):
                    self.heightsToNums.append(1)
                else:
                    self.heightsToNums[h]+=1
                self.indexToTreeNode[cur.val] = cur
                self.indexToHeight[cur.val] = h
                dfs(self,cur.left, h + 1)
                dfs(self,cur.right, h + 1)
        dfs(self,root, 0)
        self.height = len(self.heightsToNums)-1
        
        def delete(self, cur):
            if cur!=None:
                self.heightsToNums[self.indexToHeight[cur.val]] -= 1
                if self.heightsToNums[self.indexToHeight[cur.val]] == 0:
                    self.height = min(self.height, self.indexToHeight[cur.val]-1)
                if cur.val in self.indexToTreeNode:
                    del self.indexToTreeNode[cur.val]
                delete(self,cur.left)
                delete(self,cur.right)
        
        ret = []
        for query in queries:
            delete(self, self.indexToTreeNode.get(query))
            ret.append(self.height)
        return ret
