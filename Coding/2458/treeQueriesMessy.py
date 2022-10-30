# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        self.valToHeight = {}
        self.valToDepth = {}
        # key: height; value: (maxHeight, secondMaxHeight)
        self.heightToTwoMax = {}
        self.valToRealHeight = {}
        
        def precompute(cur, height):
            if cur==None:
                return height - 1
            else:
                leftHeight = precompute(cur.left, height+1)
                rightHeight = precompute(cur.right, height+1)
                self.valToHeight[cur.val] = max(leftHeight, rightHeight)
                self.valToDepth[cur.val] = max(leftHeight, rightHeight) - height + 1
                self.valToRealHeight[cur.val] = height
                return max(leftHeight, rightHeight)
        self.height = precompute(root, 0)
        
        def precompute2(cur, height):
            if cur==None:
                return height - 1
            else:
                leftHeight = precompute2(cur.left, height+1)
                rightHeight = precompute2(cur.right, height+1)
                if height in self.heightToTwoMax:
                    if max(leftHeight, rightHeight) > self.heightToTwoMax[height][0]:
                        self.heightToTwoMax[height] = (max(leftHeight, rightHeight), self.heightToTwoMax[height][0])
                    elif max(leftHeight, rightHeight) > self.heightToTwoMax[height][1]:
                        self.heightToTwoMax[height] = (self.heightToTwoMax[height][0], max(leftHeight, rightHeight)) 
                else:
                    self.heightToTwoMax[height] = (max(leftHeight, rightHeight), height-1)
                        
                return max(leftHeight, rightHeight)
        precompute2(root, 0)
        
        ret = []
        print(self.heightToTwoMax)
        for q in queries:
            if self.valToHeight[q]==self.height:
                ret.append(self.heightToTwoMax[self.valToRealHeight[q]][1])
            else:
                ret.append(self.height)
        return ret
            
