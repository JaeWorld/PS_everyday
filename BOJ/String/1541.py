# BOJ 1541 잃어버린 괄호

# 문자열

import sys
input = sys.stdin.readline

s = input()
p = []
temp = ''

for i in range(len(s)):
    if i == len(s)-1:
        p.append(int(temp))
    if s[i] == '-' or s[i] == '+':
        p.append(int(temp))
        p.append(s[i])
        temp = ''
    else:
        temp += s[i]

res = p[0]
flag = False

for i in range(1, len(p)-1):
    if p[i] == '-':
        flag = True
        res += -1*p[i+1]
    elif p[i] == '+':
        if flag:
            res += -1*p[i+1]
        else:
            res += p[i+1]

print(res)
