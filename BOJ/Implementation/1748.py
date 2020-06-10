# BOJ 1748 수 이어 쓰기 1

# 구현, 브루트포스

import sys
input = sys.stdin.readline


def main():
    n = int(input())
    d = int(len(str(n)))
    res = 0

    for i in range(1, d):
        res += i*(9*(10**(i-1)))

    res += d*(n-(10**(d-1))+1)

    print(res)


main()
