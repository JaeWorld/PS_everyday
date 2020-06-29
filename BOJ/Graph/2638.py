# BOJ 2638 치즈

# BFS

# 유의할점: 치즈 내부에 있는 공간과 외부에 있는 공간을 구별하기 위해
# (0, 0)에서부터 bfs를 돌려 외부 공간을 -1로 표시한다.

import sys
from collections import deque
input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(y, x):
    visited = [[0]*m for _ in range(n)]
    queue = deque()
    queue.append([y, x])
    visited[y][x] = 1
    mat[y][x] = -1

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if ny<0 or nx<0 or ny>=n or nx>=m:
                continue
            if not visited[ny][nx] and mat[ny][nx] != 1:
                visited[ny][nx] = 1
                queue.append([ny, nx])
                mat[ny][nx] = -1
    

def search(mat):
    melt = []
    for y in range(n):
        for x in range(m):
            if mat[y][x] == 1:
                temp = 0
                for i in range(4):
                    ny, nx = y+dy[i], x+dx[i]
                    if mat[ny][nx] == -1:
                        temp += 1
                if temp >= 2:
                    melt.append([y, x])
    
    return melt

def remove(mat, melt):
    for i in range(len(melt)):
        y, x = melt[i]
        mat[y][x] = 0
    return mat 

def checkEmpty(mat):
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 1:
                return False
    return True
                    

n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
res = 0

while True:
    if checkEmpty(mat):
        break
    bfs(0, 0)
    melt = search(mat)
    mat = remove(mat, melt)
    res += 1

print(res)
