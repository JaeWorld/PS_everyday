# BOJ 4386 별자리 만들기

# MST 알고리즘
# 크루스칼 알고리즘

import sys
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


def sameParent(x, y):
    return find(x) == find(y)


def main():
    global parent
    n = int(input())
    loc = [list(map(float, input().split())) for _ in range(n)]
    dist = []
    parent = [0]*(n+1)
    res = 0

    for i in range(1, n+1):
        parent[i] = i

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            d = getDist(loc[i], loc[j])
            dist.append([round(d, 2), i, j])

    dist.sort()

    for i in range(len(dist)):
        w, u, v = dist[i]
        if not sameParent(u, v):
            merge(u, v)
            res += w

    print(res)


main()
