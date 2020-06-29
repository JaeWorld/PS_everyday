# BOJ 1016 제곱 ㄴㄴ 수

import sys
input = sys.stdin.readline

def main():
    a, b = map(int, input().split())
    tmp = 4
    cache = [0]*(b-a+1)
    idx = 2
    cnt = 0

    while tmp <= b:
        start = (a//tmp)*tmp if a % tmp == 0 else (a//tmp)*tmp + tmp
        for i in range(start, b+1, tmp):
            if i-a < 0:
                continue
            if not cache[i-a]:
                cache[i-a] = 1
                cnt += 1
        tmp = tmp + (2*idx+1)
        idx += 1

    print((b-a+1) - cnt)

main()
