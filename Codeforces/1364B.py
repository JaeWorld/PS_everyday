import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    res = [p[0]]
    inc = True
    prev = p[0]
 
    if p[0] > p[1]:
        inc = False
 
    for i in range(1, n):
        if inc and prev > p[i]:
            res.append(prev)
            inc = False
        if not inc and prev < p[i]:
            res.append(prev)
            inc = True
        prev = p[i]
 
    res.append(p[n-1])
 
    print(len(res))
    print(*res)
