# 13549 숨바꼭질 3

# Graph, BFS

from collections import deque
import sys
input = sys.stdin.readline

MAX = 100001

def bfs(start, k):
    queue = deque()
    queue.append([start, 1])
    visited = [0]*(MAX)
    visited[start] = 1

    while queue:
        curr, time = queue.popleft()
        if curr == k:
            return visited[k]-1

        if curr*2 < MAX:
            if not visited[curr*2]:
                visited[curr*2] = time
                queue.append([curr*2, time])
            else:
                if visited[curr*2] > time:
                    visited[curr*2] = time
                    queue.append([curr*2, time])
                    
        if 0 <= curr+1 < MAX:
            if not visited[curr+1]:
                visited[curr+1] = time+1
                queue.append([curr+1, time+1])
            else:
                if visited[curr+1] > time+1:
                    visited[curr+1] = time+1
                    queue.append([curr-1, time+1])
                
        if 0 <= curr-1 < MAX:
            if not visited[curr-1]:
                visited[curr-1] = time+1
                queue.append([curr-1, time+1])
            else:
                if visited[curr-1] > time+1:
                    visited[curr-1] = time+1
                    queue.append([curr-1, time+1])

if __name__ == "__main__":
    n, k = map(int, input().split())
    print(bfs(n, k))
