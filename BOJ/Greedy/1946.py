# BOJ 1946 신입 사원

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    c = [list(map(int, input().split())) for _ in range(n)]
    c.sort()
    cnt = 0
    maxB = 100001

    for i in range(n):
        if c[i][1] < maxB:
            maxB = c[i][1]
            cnt += 1

    print(cnt)
