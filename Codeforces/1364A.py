import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    s, e = -1, -1
    val = sum(a)
 
    if val % x != 0:
        print(n)
        continue
 
    for i in range(n):
        if a[i] % x != 0:
            s = i
            break
 
    for i in range(n-1, -1, -1):
        if a[i] % x != 0:
            e = i
            break
 
    if s == -1:
        print(-1)
    else:
        print(max(n-s-1, e))
