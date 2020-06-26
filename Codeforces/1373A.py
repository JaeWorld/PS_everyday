# Codeforces 1373A

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    res1, res2 = 0, 0

    if a >= c:
        res1 = -1
    else:
        res1 = 1

    if a*b <= c:
        res2 = -1
    else:
        res2 = b
 
    print(res1, res2)
