# BOJ 2234 성곽

# BFS

import sys
from collections import deque

dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]


def bfs(y, x):
    visited[y][x] = 1
    queue = deque()
    queue.append([y, x])
    count = 1

    while queue:
        y, x = queue.popleft()
        pos = mat[y][x]
        movements = walls[pos]
        if len(movements) == 0:
            continue
        for mv in movements:
            ny = y+dy[mv]
            nx = x+dx[mv]
            if ny < 0 or nx < 0 or ny >= m or nx >= n:
                continue
            if visited[ny][nx]:
                continue
            visited[ny][nx] = 1
            count += 1
            queue.append([ny, nx])

    return count


n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(m)]
walls = {0: [0, 1, 2, 3], 1: [1, 2, 3], 2: [0, 2, 3], 3: [2, 3], 4: [0, 1, 3], 5: [1, 3], 6: [0, 3], 7: [
    3], 8: [0, 1, 2], 9: [1, 2], 10: [0, 2], 11: [2], 12: [0, 1], 13: [1], 14: [0], 15: []}
visited = [[0]*n for _ in range(m)]
d = [1, 2, 4, 8]
rooms = []
res = 0

for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            temp = bfs(i, j)
            rooms.append(temp)

for i in range(m):
    for j in range(n):
        curr = mat[i][j]
        w = walls[curr]
        for k in range(4):
            if k in w:
                continue
            visited = [[0]*n for _ in range(m)]
            mat[i][j] -= d[k]
            size = bfs(i, j)
            mat[i][j] += d[k]

            if size > res:
                res = size

print(len(rooms))
print(max(rooms))
print(res)
