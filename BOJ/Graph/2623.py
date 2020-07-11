# BOJ 2623 음악프로그램

# 위상 정렬

import sys
input = sys.stdin.readline
from collections import deque

def topologicalSort():
    res = []
    queue = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            queue.append(i)

    for i in range(1, n+1):
        if not queue:
            print(0)
            return 0

        curr = queue.pop()
        res.append(curr)
        for adj in graph[curr]:
            indegree[adj] -= 1
            if indegree[adj] == 0:
                queue.append(adj)

    print(*res[::-1], sep="\n")

if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    indegree = [0]*(n+1)

    for _ in range(m):
        l = list(map(int, input().split()))
        for i in range(1, l[0]):
            graph[l[i+1]].append(l[i])
            indegree[l[i]] += 1
            
    topologicalSort()
