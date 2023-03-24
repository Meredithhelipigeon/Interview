# Time Complexity: O(E+V)
# Space Complexity: O(E+V)
class Solution1:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        neighbours = [[] for i in range(n)]
        visited = [False]*n
        ret = 0
        
        def bfs(start):
            q = Queue()
            q.put(start)
            visited[start]=True
            
            while q.qsize()>0:
                curNode = q.get()
                for n in neighbours[curNode]:
                    if not visited[n]:
                        q.put(n)
                        visited[n]=True
        
        # preprocess neighbours
        for e in edges:
            node1, node2 = e
            neighbours[node1].append(node2)
            neighbours[node2].append(node1)
        
        # calculate results
        for i in range(n):
            if visited[i]==False:
                bfs(i)
                ret += 1
        return ret
