# BOJ 9466. 텀 프로젝트
# dfs로 탐색하며 route를 기록.
# 만약 사이클이 있는 경우, route에서 사이클 부분의 길이를 구함.

import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
global s, cycleCnt
global visited, parent

def dfs(x):
    global cycleCnt
    visited[x] = 1
    route.append(x)
    nxt = s[x]
    if not visited[nxt]:
        dfs(nxt)
    else:
        if nxt in route:
            cycleCnt += len(route[route.index(nxt):])
            return

if __name__=='__main__':
    T = int(input())
    for _ in range(T):
        n = int(input())
        s = [0]+list(map(int, input().split()))
        visited = [0]*(n+1)
        parent = [0]*(n+1)
        cycleCnt = 0
        
        for i in range(1, n+1):
            if not visited[i]:
                route = []
                dfs(i)

        print(n-cycleCnt)
