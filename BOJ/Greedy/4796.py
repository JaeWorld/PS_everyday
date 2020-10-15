# BOJ 4796 캠핑

# 그리디
# 수학

import sys
input = sys.stdin.readline

idx = 0
while True:
    L, P, V = map(int, input().split())
    if L == 0:
        break
    ans = 0
    idx += 1

    ans += L * (V // P)
    ans += min(V % P, L)

    print(f'Case {idx}: {ans}')
