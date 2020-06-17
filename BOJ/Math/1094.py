# BOJ 1094 막대기

# 수학

import sys
input = sys.stdin.readline

x = int(input())
d = []
s = 64
res, count = 0, 0

while s > 0:
    d.append(s)
    s = s//2

for i in range(len(d)):
    if res + d[i] <= x:
        res += d[i]
        count += 1
    if res == x:
        print(count)
        break
