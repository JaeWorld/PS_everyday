# BOJ 1049 기타줄

import sys
input = sys.stdin.readline

def main():
  n, m = map(int, input().split())
  bp, bi = 987654321, 987654321
  res = 0

  for i in range(m):
    pack, ind = map(int, input().split())
    bp = min(bp, pack)
    bi = min(bi, ind)

  if bp < bi*6:
    res = min(bp*(n//6)+bi*(n%6), bp*(n//6+1))
  else:
    res = bi*n

  print(res)

main()
