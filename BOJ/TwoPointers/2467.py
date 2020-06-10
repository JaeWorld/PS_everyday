# BOJ 2467 용액

# 투포인터

import sys
input = sys.stdin.readline

def main():
    n = int(input())
    a = list(map(int, input().split()))
    s, e = 0, n-1
    x, y = 0, 0
    prev = 2000000000

    while True:
        curr = a[s]+a[e]
        if abs(curr) == 0:
            x, y = a[s], a[e]
            break
        if abs(curr) < prev:
            x, y = a[s], a[e]
            prev = abs(curr)
        elif curr < 0:
            s += 1
        elif curr > 0:
            e -= 1
        if s == e:
            break

    print(x, y)

main()
