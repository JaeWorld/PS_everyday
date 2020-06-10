# BOJ 1774 우주신과의 교감

# MST 알고리즘
# 크루스칼 알고리즘

import sys
import heapq
input = sys.stdin.readline


def getDist(a, b):
    x1, y1 = a
    x2, y2 = b
    return ((x1-x2)**2 + (y1-y2)**2)**0.5


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


def main():
    n, m = map(int, input().split())
    loc = [list(map(int, input().split())) for _ in range(n)]
    dist = []
    global parent
    parent = [0]*(n+1)
    res = 0

    for i in range(1, n+1):
        parent[i] = i

    for i in range(m):
        link = list(map(int, input().split()))
        merge(link[0], link[1])

    for i in range(n):
        for j in range(n):
            if find(i+1) == find(j+1):
                continue
            heapq.heappush(dist, [getDist(loc[i], loc[j]), i+1, j+1])

    for i in range(len(dist)):
        curr = heapq.heappop(dist)
        if find(curr[1]) != find(curr[2]):
            merge(curr[1], curr[2])
            res += curr[0]

    print(format(res, ".2f"))


main()
