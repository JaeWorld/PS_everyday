# BOJ 18265 MooBuzz

# 수학

import sys
input = sys.stdin.readline

def main():
    n = int(input())
    a = n//8 if n % 8 != 0 else n//8-1
    b = n % 8 if n % 8 != 0 else 8
    count = 0

    for i in range(15*a+1, 15*(a+1)+1):
        if i % 3 != 0 and i % 5 != 0:
            count += 1
        if count == b:
            print(i)
            break

main()
