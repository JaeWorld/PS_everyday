# BOJ 11123 양 한마리... 양 두마리...

# Graph, BFS

from collections import deque
import sys
input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(y, x):
    queue = deque()
    queue.append([y, x])
    visited[y][x] = 1
    
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if ny < 0 or nx < 0 or ny >= h or nx >= w:
                continue
            if not visited[ny][nx] and g[ny][nx] == '#':
                queue.append([ny, nx])
                visited[ny][nx] = 1

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        h, w = map(int, input().split())
        g = [list(input().strip()) for _ in range(h)]
        visited = [[0]*w for _ in range(h)]
        ans = 0
        for i in range(h):
            for j in range(w):
                if not visited[i][j] and g[i][j] == '#':
                    bfs(i, j)
                    ans += 1

        print(ans)
