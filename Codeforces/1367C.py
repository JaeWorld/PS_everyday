# Codeforces 1367C

import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = list(input())[:-1]
    res = 0
 
    for i in range(n):
        if s[i] == "1":
            for j in range(i-k, i+k+1):
                if j >= 0 and j < n:
                    s[j] = "-1"
 
    for i in range(n):
        if s[i] == "0":
            res += 1
            for j in range(i, i+k+1):
                if j >= 0 and j < n:
                    s[j] = "-1"
 
    print(res)
