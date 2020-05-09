# Codeforces 1324A

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    res = "YES"

    piv = a[0] % 2
    for i in range(1, len(a)):
        if a[i] % 2 != piv:
            res = "NO"
            break

    print(res)
