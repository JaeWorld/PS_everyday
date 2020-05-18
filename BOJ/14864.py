# BOJ 14864 줄서기

import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    l = [list(map(int, input().split())) for _ in range(m)]
    d = [0]*(n+1)
    a = [0]*(n+1)
    visited = [0]*(n+1)
    flag = True

    for i in range(m):
        x, y = l[i]
        d[x] += 1
        d[y] -= 1

    for i in range(1, n+1):
        a[i] = i + d[i]

        if visited[a[i]] == 0:
            visited[a[i]] = 1
        elif visited[a[i]] == 1:
            flag = False
            break

    if flag:
        print(*a[1:])
    else:
        print(-1)

main()
