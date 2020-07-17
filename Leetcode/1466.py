# Leetcode 1466. Reorder Routes to Make All Paths Lead to the City Zero

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        edges = set()
        visited = [0]*(n+1)
        self.ans = 0
        
        for i in range(n-1):
            a, b = connections[i]
            graph[a].append(b)
            graph[b].append(a)
            edges.add((a, b))
            
        def dfs(v):
            visited[v] = 1
            for adj in graph[v]:
                if not visited[adj]:
                    if (v, adj) in edges:
                        self.ans += 1
                    dfs(adj)
                
        dfs(0)
        return self.ans
