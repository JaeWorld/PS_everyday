# BOJ 13418 학교 탐방하기

# MST 알고리즘
# 크루스칼 알고리즘

'''
C를 기준으로 오름차순, 내림차순으로 각각 정렬하여
크루스칼 알고리즘으로 두 경우의 피로도를 계산한다.
'''

import sys
input = sys.stdin.readline


def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def merge(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x


def sameParent(x, y):
    return find(x) == find(y)


def solve(links, k):
    res = 0
    for i in range(n+1):
        parent[i] = i

    # 오르막길 => 내리막길 순 정렬
    if k == 0:
        links.sort(key=lambda x: x[2])
    # 내리막길 => 오르막길 순 정렬
    elif k == 1:
        links.sort(key=lambda x: -x[2])

    for link in links:
        a, b, c = link
        if a == 0 or b == 0:
            res += (1-c)
            continue
        if not sameParent(a, b):
            merge(a, b)
            res += (1-c)

    return res**2


n, m = map(int, input().split())
links = [list(map(int, input().split())) for _ in range(m+1)]
parent = [0]*(n+1)
best = solve(links, 1)
worst = solve(links, 0)

print(worst-best)
