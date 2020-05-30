# BOJ 10656 십자말풀이

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
mat = [list(input()) for _ in range(n)]
res = []

for i in range(n):
    for j in range(m):
        horiFlag = False
        vertFlag = False
        if mat[i][j] == '#':
            continue

        if j-1 < 0 or mat[i][j-1] == '#':
            if j+2 < m:
                if mat[i][j+1] == '.' and mat[i][j+2] == '.':
                    horiFlag = True
                else:
                    horiFlag = False

        if i-1 < 0 or mat[i-1][j] == '#':
            if i+2 < n:
                if mat[i+1][j] == '.' and mat[i+2][j] == '.':
                    vertFlag = True
                else:
                    vertFlag = False

        if horiFlag or vertFlag:
            res.append([i+1, j+1])

print(len(res))
for i in range(len(res)):
    print(*res[i])
