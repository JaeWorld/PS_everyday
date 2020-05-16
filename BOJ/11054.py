# BOJ 11054 가장 긴 바이토닉 부분 수열

# 동적계획법
# LIS 알고리즘 변형

import sys
input = sys.stdin.readline


def main():
    n = int(input())
    a = list(map(int, input().split()))
    dpInc = [0]*n
    dpDec = [0]*n
    res = 0

    for i in range(n):
        if dpInc[i] == 0:
            dpInc[i] = 1
        for j in range(i):
            if a[j] < a[i]:
                dpInc[i] = max(dpInc[i], dpInc[j]+1)

    for i in range(n-1, -1, -1):
        if dpDec[i] == 0:
            dpDec[i] = 1
        for j in range(i, n):
            if a[j] < a[i]:
                dpDec[i] = max(dpDec[i], dpDec[j]+1)

    for i in range(n):
        if dpInc[i] + dpDec[i] > res:
            res = dpInc[i] + dpDec[i]

    print(res-1)

main()
