# BOJ 2631

import sys
input = sys.stdin.readline

def main():
  n = int(input())
  s = [int(input()) for _ in range(n)]
  dp = [1]*n

  for i in range(n):
    for j in range(i):
      if s[i] > s[j]:
        dp[i] = max(dp[i], dp[j]+1)
    
  print(n-max(dp))

main()
