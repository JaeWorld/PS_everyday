# Codeforces 1365A 

# Greedy

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(n)]
    r = []
    c = []

    for i in range(n):
        for j in range(m):
            if mat[i][j] == 1:
                if j not in r:
                    r.append(j)
                if i not in c:
                    c.append(i)

    claims = min(n-len(c), m-len(r))

    print('Ashish' if claims % 2 == 1 else 'Vivek')
