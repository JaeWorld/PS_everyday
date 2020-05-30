# BOJ 14467 소가 길을 건너간 이유 1

import sys
input = sys.stdin.readline

n = int(input())
pos = {}
res = 0

for i in range(n):
    c, p = map(int, input().split())
    if c in pos:
        if pos[c][-1] != p:
            res += 1
        pos[c].append(p)
    else:
        pos[c] = [p]

print(res)
