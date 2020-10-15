# BOJ 1520 내리막 길

# DP, DFS

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

m, n = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(m)]
check = [[-1]*n for _ in range(m)]

def dfs(y, x):
    if y == m-1 and x == n-1:
        return 1
    
    if check[y][x] != -1:
        return check[y][x]
    
    check[y][x] = 0
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny >= m or ny < 0 or nx >= n or nx < 0:
            continue
        if mat[y][x] > mat[ny][nx]:
            check[y][x] += dfs(ny, nx)

    return check[y][x]

print(dfs(0, 0))
