# BOJ 9994 Secret Code

# 재귀

import sys

def func(s):
    l = len(s)
    res = 1
    if l % 2 == 0 or l == 1:
        return 1

    if s[:l//2] == s[l//2:l-1]:
        res += func(s[l//2:])

    if s[:l//2] == s[l//2+1:l]:
        res += func(s[:l//2+1])

    if s[:l//2] == s[l//2+1:l]:
        res += func(s[l//2:])

    if s[1:l//2+1] == s[l//2+1:l]:
        res += func(s[:l//2+1])

    return res

a = input()
print(func(a)-1)
