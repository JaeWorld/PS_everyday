# BOJ 3036 링

# 수학

import sys
input = sys.stdin.readline

def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

n = int(input())
a = list(map(int, input().split()))

for i in range(1, n):
    g = gcd(a[0], a[i])
    print("{}/{}".format(a[0]//g, a[i]//g))
