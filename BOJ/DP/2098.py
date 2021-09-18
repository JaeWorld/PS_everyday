# BOJ 2098. 외판원 순회

import sys
input = sys.stdin.readline


def travel(curr, visited):
    if visited == (1<<n)-1:
        d = dist[curr][start]
        return d if d != 0 else INF
    if dp[curr][visited] != -1:
        return dp[curr][visited]
    
    dp[curr][visited] = INF
    for nxt in range(n):
        if visited & (1<<nxt):
            continue
        if dist[curr][nxt] == 0:
            continue
        dp[curr][visited] = min(dp[curr][visited], dist[curr][nxt] + travel(nxt, (1<<nxt)|visited))
    return dp[curr][visited]

if __name__=='__main__':
    n = int(input())
    dist = [list(map(int, input().split())) for _ in range(n)]
    dp = [[-1]*(2**n+1) for _ in range(n)]
    start = 0
    INF = 987654321

    print(travel(0, 1))
