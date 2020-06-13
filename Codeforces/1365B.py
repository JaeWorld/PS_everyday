# Codeforces 1365B

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if sorted(a) == a:
        print('Yes')
    else:
        zeroCount = b.count(0)
        oneCount = b.count(1)
        if zeroCount >= 1 and oneCount >= 1:
            print('Yes')
        else:
            print('No')
