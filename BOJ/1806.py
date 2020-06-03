# BOJ 1806 부분합

# 투포인터

import sys
input = sys.stdin.readline

def main():
  n, s = map(int, input().split())
  a = list(map(int, input().split()))
  hi, lo = 0, 0
  temp = 0
  length = []

  while True:
    if temp >= s:
      length.append(hi-lo)
      temp -= a[lo]
      lo += 1
    elif hi == n:
      break
    elif temp < s:
      temp += a[hi]
      hi += 1

  if length:
    print(min(length))
  else:
    print(0)
  
main()
