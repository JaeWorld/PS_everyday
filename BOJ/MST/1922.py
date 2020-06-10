# BOJ 1922 네트워크 연결

# MST 알고리즘, 크루스칼 알고리즘
# 유니온 파인드를 이용

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
    x = find(x)
    y = find(y)

    if x == y:
        return True
    else:
        return False


n = int(input())
m = int(input())
links = [list(map(int, input().split())) for _ in range(m)]
parent = [0]*(n+1)
res = 0
links.sort(key=lambda x: x[2])

for i in range(1, n+1):
    parent[i] = i

for i in range(m):
    u, v, w = links[i]
    if not sameParent(u, v):
        merge(u, v)
        res += w

print(res)
