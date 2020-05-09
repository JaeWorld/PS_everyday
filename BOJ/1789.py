# BOJ 1789 수들의 합

import sys
input = sys.stdin.readline

s = int(input())
temp = 0
count = 0
for i in range(1, s):
    if temp + i >= s and s - temp < i:
        break
    temp += i
    count += 1

print(count)
