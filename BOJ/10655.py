# BOJ 10655 마라톤 1

import sys
input = sys.stdin.readline

def getDist(a, b):
    x1, y1 = a
    x2, y2 = b
    return abs(x1-x2) + abs(y1-y2)

def main():
    n = int(input())
    p = [list(map(int, input().split())) for _ in range(n)]
    totalDist = getDist(p[0], p[1])
    skip = 0

    for i in range(1, n-1):
        prev, curr, nxt = p[i-1], p[i], p[i+1]
        totalDist += getDist(curr, nxt)
        normalDist = getDist(prev, curr) + getDist(curr, nxt)
        skippedDist = getDist(prev, nxt)

        if normalDist - skippedDist > skip:
            skip = normalDist - skippedDist

    print(totalDist - skip)

main()
