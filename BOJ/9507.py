# BOJ 9507 Generations of Tribbles

import sys
input = sys.stdin.readline

def fib(n):
    if n < 2:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    if dp[n] != -1:
        return dp[n]

    dp[n] = fib(n-1) + fib(n-2) + fib(n-3) + fib(n-4)
    return dp[n]

t = int(input())
for _ in range(t):
    n = int(input())
    dp = [-1]*(n+1)

    print(fib(n))
