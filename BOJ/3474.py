# BOJ 3474
# 5가 1번(5^1 = 5) 들어있는 모든 수 개수 더해주고
# 5가 한번 더(5^2 = 25) 들어있는 모든 수 개수 더해주고
# 5가 한번 더(5^3 = 125) 들어있는 모든 수 개수 더해주는 방식
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    five = 0
    i = 5

    while i <= n:
        five += n//i
        i *= 5

    print(five)
