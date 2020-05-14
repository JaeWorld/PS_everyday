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
