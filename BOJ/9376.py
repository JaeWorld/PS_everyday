# BOJ 9376 탈옥

# BFS

from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def bfs(y, x):
    visited = [[-1]*(w+2) for _ in range(h+2)]
    queue = deque()
    queue.append([y, x])
    visited[y][x] = 0

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if ny < 0 or ny > h+1 or nx < 0 or nx > w+1:
                continue
            if visited[ny][nx] >= 0 or m[ny][nx] == '*':
                continue
            if m[ny][nx] == '#':
                visited[ny][nx] = visited[y][x]+1
                queue.append([ny, nx])
            if m[ny][nx] == '.' or m[ny][nx] == '$':
                visited[ny][nx] = visited[y][x]
                queue.appendleft([ny, nx])

    return visited


t = int(input())
for _ in range(t):
    h, w = map(int, input().split())
    m = [list('.'*(w+2))]
    m.extend([['.']+list(input())+['.'] for _ in range(h)])
    m.extend([list('.'*(w+2))])
    p = []
    ans = 987654321

    for i in range(h+2):
        for j in range(w+2):
            if m[i][j] == '$':
                p.append([i, j])

    y1, x1 = p.pop()
    v1 = bfs(y1, x1)

    y2, x2 = p.pop()
    v2 = bfs(y2, x2)

    v3 = bfs(0, 0)

    for i in range(h+2):
        for j in range(w+2):
            if m[i][j] == '*':
                continue
            temp = v1[i][j] + v2[i][j] + v3[i][j]
            if m[i][j] == '#':
                temp -= 2
            ans = min(ans, temp)

    print(ans)
