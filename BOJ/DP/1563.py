# BOJ 1563 개근상

import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


def func(d, l, a):
    if l == 2 or a == 3:
        return 0
    if d == n:
        return 1
    if dp[d][l][a] != -1:
        return dp[d][l][a]

    dp[d][l][a] = (func(d+1, l, 0) + func(d+1, l+1, 0) +
                   func(d+1, l, a+1)) % 1000000
    return dp[d][l][a]


n = int(input())
dp = [[[-1]*(3) for _ in range(4)] for _ in range(n+1)]

func(0, 0, 0)
print(dp[0][0][0])
