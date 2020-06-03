# BOJ 7453 합이 0인 네 정수

import sys
input = sys.stdin.readline

def main():
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    res = 0

    ab = {}
    cd = {}

    for i in range(n):
        for j in range(n):
            if arr[i][0] + arr[j][1] not in ab.keys():
                ab[arr[i][0] + arr[j][1]] = 1
            else:
                ab[arr[i][0] + arr[j][1]] += 1

            if arr[i][2] + arr[j][3] not in cd.keys():
                cd[arr[i][2] + arr[j][3]] = 1
            else:
                cd[arr[i][2] + arr[j][3]] += 1

    for k in ab:
        if -k in cd:
            res += ab[k] * cd[-k]

    print(res)

main()
