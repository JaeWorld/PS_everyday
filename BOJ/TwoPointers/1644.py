# BOJ 1644 소수의 연속합

# 투포인터

import sys

def primeNet(n, nums):
  a = []
  for i in range(2, n+1):
    if nums[i] == 0:
      continue
    for j in range(2*i, n+1, i):
      nums[j] = 0

  for i in range(n+1):
    if nums[i] != 0:
      a.append(nums[i])

  return a

def main():
  n = int(sys.stdin.readline())
  s, e, temp, res = 0, 0, 0, 0
  nums = [x for x in range(n+1)]
  nums[1] = 0
  a = primeNet(n, nums)
  
  while True:
    if temp >= n:
      temp -= a[s]
      s += 1
    elif e == len(a):
      break
    elif temp < n:
      temp += a[e]
      e += 1
    if temp == n:
      res += 1

  print(res)

main()
