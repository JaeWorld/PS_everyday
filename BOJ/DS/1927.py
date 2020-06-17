# BOJ 1927 최소 힙

# 자료구조

import sys
import heapq
input = sys.stdin.readline

n = int(input())
q = []
for _ in range(n):
    x = int(input())
    if x == 0:
        if q:
            print(heapq.heappop(q))
        else:
            print(0)
    elif x > 0:
        heapq.heappush(q, x)
