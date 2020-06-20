# BOJ 11660 구간 합 구하기 5

# DP

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
t = [list(map(int, input().split())) for _ in range(m)]
dp = [[0]*n for _ in range(n)]
dp[0][0] = a[0][0]

for i in range(1, n):
    dp[0][i] = dp[0][i-1] + a[0][i]

for i in range(1, n):
    for j in range(n):
        if j>=1:
            dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + a[i][j]
        else:
            dp[i][j] = dp[i-1][j] + a[i][j]

for i in range(m):
    x1, y1, x2, y2 = t[i]
    if x1 >= 2 and y1 >= 2:
        res = dp[x2-1][y2-1] - (dp[x1-2][y2-1] + dp[x2-1][y1-2] - dp[x1-2][y1-2])
    elif y1 == 1 and x1 == 1:
        res = dp[x2-1][y2-1]
    elif y1 == 1:
        res = dp[x2-1][y2-1] - dp[x1-2][y2-1]
    elif x1 == 1:
        res = dp[x2-1][y2-1] - dp[x2-1][y1-2]

    print(res)
