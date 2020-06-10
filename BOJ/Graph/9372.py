# BOJ 9372 상근이의 여행

# MST 풀이

import sys
input = sys.stdin.readline

def find(x):
  if parent[x] == x:
    return x
  parent[x] = find(parent[x])
  return parent[x]

def merge(x, y):
  x = find(x)
  y = find(y)

  if x != y:
    parent[y] = x
  
def sameParent(x, y):
  return find(x) == find(y)

t = int(input())
for _ in range(t):
  n, m = map(int, input().split())
  links = [list(map(int, input().split())) for _ in range(m)]
  parent = [0]*(n+1)
  res = 0

  for i in range(1, n+1):
    parent[i] = i

  for link in links:
    a, b = link
    if not sameParent(a, b):
      merge(a, b)
      res += 1
    
  print(res)
  
  
# BFS 풀이

import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
  visited = [0]*(n+1)
  visited[start] = 1
  queue = deque()
  queue.append(start)
  count = 0

  while queue:
    curr = queue.popleft()
    for adj in graph[curr]:
      if not visited[adj]:
        queue.append(adj)
        visited[adj] = 1 
        count += 1

  return count

t = int(input())
for _ in range(t):
  n, m = map(int, input().split())
  links = [list(map(int, input().split())) for _ in range(m)]
  graph = [[] for _ in range(n+1)]

  for link in links:
    a, b = link
    graph[a].append(b)
    graph[b].append(a)

  res = bfs(1)

  print(res)
