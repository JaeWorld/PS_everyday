# Codeforces 1352A 

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    res = []
    i = 0

    while n > 0:
        if n % 10 > 0:
            res.append((n % 10 * 10**i))
        i += 1
        n = n//10

    print(len(res))
    print(*res)
