# BOJ 2666 벽장문의 이동

# DP

import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
if a > b:
    a, b = b, a
l = int(input())
order = [int(input()) for _ in range(l)]
dp = [[[-1]*(n+1) for _ in range(n+1)] for _ in range(l)]

def func(idx, o1, o2):
    if idx > l-1:
        return 0
    res = dp[idx][o1][o2]
    if res != -1:
        return res
    
    tgt = order[idx]
    if tgt < o1:
        res = func(idx+1, tgt, o2) + abs(o1-tgt)
    elif tgt > o2:
        res = func(idx+1, o1, tgt) + abs(o2-tgt)
    else:
        res = min(abs(o1-tgt) + func(idx+1, tgt, o2), abs(o2-tgt) + func(idx+1, o1, tgt))
    return res
    
print(func(0, a, b))
