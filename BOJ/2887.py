# BOJ 2887 행성 터널

# MST 알고리즘
# 크루스칼 알고리즘

'''
x, y, z 좌표 순으로 각각 정렬한 다음, 
i 행성과 i+1 행성의 거리로 터널 리스트를 생성하여,
크루스칼 알고리즘을 돌린다.
'''

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


def getTunnel(dist, key):
    t = []
    for i in range(len(dist)-1):
        t.append([abs(dist[i][key]-dist[i+1][key]), dist[i][3], dist[i+1][3]])
    return t


def main():
    global parent
    n = int(input())
    dist = [list(map(int, input().split())) + [i] for i in range(n)]
    tunnels = []
    parent = [0]*n
    res = 0

    for i in range(n):
        parent[i] = i

    dist.sort()
    tunnels.extend(getTunnel(dist, 0))
    dist.sort(key=lambda x: x[1])
    tunnels.extend(getTunnel(dist, 1))
    dist.sort(key=lambda x: x[2])
    tunnels.extend(getTunnel(dist, 2))

    tunnels.sort()

    count = 0

    for i in range(len(tunnels)):
        w, u, v = tunnels[i]
        if not sameParent(u, v):
            merge(u, v)
            count += 1
            res += w
        if count == n-1:
            break

    print(res)


main()
