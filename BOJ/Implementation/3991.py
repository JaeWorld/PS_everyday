# BOJ 한번 쏘면 멈출 수 없어

# 구현

import sys
input = sys.stdin.readline

h, w, c = map(int, input().split())
l = list(map(int, input().split()))

ans = [[0]*w for _ in range(h)]

l_dic = sorted(list(enumerate(l, 1)), key=lambda x: -x[1])
pos = 0

for i in range(c):
    color, cnt = l_dic[i]
    for j in range(pos, pos+cnt):
        row, col = j//w, j%w
        if row%2 == 1:
            col = w-col-1
        ans[row][col] = color
    pos += cnt

for i in range(h):
    for j in range(w):
        print(ans[i][j], end='')
    print()
