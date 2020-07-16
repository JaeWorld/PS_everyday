# BOJ 2167 2차원 배열의 합

import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    mat = [[0]*(m+1)] + [[0]+list(map(int, input().split())) for _ in range(n)]
    dp = [[0]*(m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + mat[i][j]

    k = int(input())
    for _ in range(k):
        i, j, x, y = map(int, input().split())
        ans = dp[x][y] - dp[i-1][y] - dp[x][j-1] + dp[i-1][j-1]
        print(ans)

