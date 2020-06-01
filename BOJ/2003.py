# BOJ 2003 수들의 합 2

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
s, e = 0, 0
temp, count = 0, 0

while True:
    if temp >= m:
        temp -= a[s]
        s += 1
    elif e == n:
        break
    else:
        temp += a[e]
        e += 1
    if temp == m:
        count += 1

print(count)
