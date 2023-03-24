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

# Time efficiency: O(V+E)
# Space complexity: O(V+E)   
class Solution2:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = [False]*n
        neighbours = [set() for i in range(n)]
        # preprocess neighbours
        for e in edges:
            neighbours[e[0]].add(e[1])
            neighbours[e[1]].add(e[0])
        
        def dfs(curNode):
            for n in neighbours[curNode]:
                if not visited[n]:
                    visited[n]=True
                    neighbours[n].remove(curNode)
                    if not dfs(n): return False
                else: return False
            return True
        
        start = 0
        visited[start]=True
        
        # no cycle and connected
        return dfs(start) and (visited.count(False)==0)
