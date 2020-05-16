# BOJ 11053 가장 긴 증가하는 부분 수열

# 동적계획법
# LIS 알고리즘

import sys
input = sys.stdin.readline

def main():
    n = int(input())
    a = list(map(int, input().split()))
    dp = [0]*n

    for i in range(n):
        if dp[i] == 0:
            dp[i] = 1
        for j in range(i):
            if a[j] < a[i]:
                dp[i] = max(dp[i], dp[j]+1)

    print(max(dp))

main()
