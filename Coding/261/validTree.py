class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        neighbours = {}
        visited = [False] * n
        
        global edgesSet 
        edgesSet = set()
        global ret
        ret = True
        
        for e in edges:
            if e[0] in neighbours:
                neighbours[e[0]].append(e[1])
            else:
                neighbours[e[0]] = [e[1]]
            if e[1] in neighbours:
                neighbours[e[1]].append(e[0])
            else:
                neighbours[e[1]] = [e[0]]
        
        def dfs(cur):
            global edgesSet 
            global ret
            if cur not in neighbours:
                return
            for neighbour in neighbours[cur]:
                if not visited[neighbour]:
                    visited[neighbour]=True
                    edgesSet.add((cur,neighbour))
                    dfs(neighbour)
                else:
                    if not (neighbour,cur) in edgesSet:
                        ret = False
       
        visited[0]= True
        dfs(0)
        for v in visited:
            if not v:
                return False  
        
        return ret
