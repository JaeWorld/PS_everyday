# BOJ 1074 Z

# 재귀

import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def func(x, y, l):
    global cnt
    if x==r and y==c:
        print(cnt)
        return
    if l == 1:
        cnt += 1
        return
    if not (x<=r<x+l and y<=c<y+l):
        cnt += l*l
        return

    func(x, y, l//2)
    func(x, y+l//2, l//2)
    func(x+l//2, y, l//2)
    func(x+l//2, y+l//2, l//2)

n, r, c = map(int, input().split())
cnt = 0
func(0, 0, 2**n)
