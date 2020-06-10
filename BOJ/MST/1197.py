# BOJ 1197 네트워크 연결

# MST 알고리즘
# 크루스칼 알고리즘 사용해 풀이

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


def main():
    v, e = map(int, input().split())
    links = [list(map(int, input().split())) for _ in range(e)]
    global parent
    parent = [0]*(v+1)
    links.sort(key=lambda x: x[2])
    res = 0

    for i in range(1, v+1):
        parent[i] = i

    for i in range(e):
        u, v, w = links[i]
        if not sameParent(u, v):
            merge(u, v)
            res += w

    print(res)


main()
