# BOJ 1124 언더프라임

import sys
input = sys.stdin.readline


def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def main():
    a, b = map(int, input().split())
    res = 0
    nums = [0]*(b+1)
    nums[1] = 1

    for i in range(2, b+1):
        if isPrime(i):
            nums[i] = 1
        elif i % 2 == 0:
            nums[i] = nums[i//2] + 1
        else:
            for j in range(3, i+1, 2):
                if i % j == 0:
                    nums[i] = nums[i//j] + 1
                    break

    for i in range(a, b+1):
        if isPrime(nums[i]):
            res += 1

    print(res)


main()
