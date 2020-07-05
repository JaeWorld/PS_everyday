# BOJ 11725 

# Graph

import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]
ans = [[] for _ in range(n+1)]

def bfs(start):
    queue = deque()
    queue.append(start)
    visited = [0]*(n+1)
    visited[start] = 1

    while queue:
        curr = queue.popleft()
        for adj in graph[curr]:
            if not visited[adj]:
                queue.append(adj)
                visited[adj] = 1
                ans[adj] = curr


for i in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

bfs(1)

print(*ans[2:], sep="\n")

