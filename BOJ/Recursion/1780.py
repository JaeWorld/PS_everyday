# BOJ 1780 종이의 개수

# 재귀, 분할정복

import sys
input = sys.stdin.readline

def check(x, y, n):
    for i in range(x, x+n):
        for j in range(y, y+n):
            if mat[x][y] != mat[i][j]:
                return False
    return True

def func(x, y, n):
    if check(x, y, n):
        ans[mat[x][y]] += 1
        return 
    m = n//3
    for i in range(3):
        for j in range(3):
            func(x+i*m, y+j*m, m)


if __name__ == "__main__":
    n = int(input())
    mat = [list(map(int, input().split())) for _ in range(n)]
    ans = {-1: 0, 0: 0, 1: 0}

    func(0, 0, n)
    for val in ans.values():
        print(val)

