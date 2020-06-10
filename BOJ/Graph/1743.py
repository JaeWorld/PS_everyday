# BOJ 1743 음식물 피하기

# DFS

import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def dfs(y, x):
    global count
    visited[y][x] = 1
    count += 1

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny >= n or ny < 0 or nx >= m or nx < 0:
            continue

        if mat[ny][nx] == '#' and not visited[ny][nx]:
            dfs(ny, nx)


n, m, k = map(int, input().split())
mat = [['.']*(m) for _ in range(n)]
visited = [[0]*(m) for _ in range(n)]
res = 0
count = 0

for i in range(k):
    r, c = map(int, input().split())
    mat[r-1][c-1] = '#'

for i in range(n):
    for j in range(m):
        if mat[i][j] == '#' and not visited[i][j]:
            count = 0
            dfs(i, j)
            if count > res:
                res = count

print(res)
