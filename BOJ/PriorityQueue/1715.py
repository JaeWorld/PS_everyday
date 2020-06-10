# BOJ 1715 카드 정렬하기

import sys
import heapq
input = sys.stdin.readline

n = int(input())
queue = []
res = 0

for _ in range(n):
    heapq.heappush(queue, int(input()))

while len(queue) > 1:
    a = heapq.heappop(queue)
    b = heapq.heappop(queue)
    res += a + b
    heapq.heappush(queue, a+b)

print(res)
