class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ret=[]
        for i in range(len(matrix[0])):
            cur=[]
            for j in range(len(matrix)):
                cur.append(matrix[j][i])
            ret.append(cur)
        return ret
