# BOJ 1111 IQ Test

# 수학

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
res = []

if n == 1:
    print('A')
elif n == 2:
    if nums[0] == nums[1]:
        print(nums[0])
    else:
        print('A')
else:
    flag = True
    a = 0
    b = 0

    for i in range(n-1):
        if i == 0:
            curr = nums[i]
            nxt = nums[i+1]
            afternxt = nums[i+2]

            if nxt - curr == 0:
                a = 0
                b = nxt - curr*a
            else:
                a = (afternxt - nxt) // (nxt - curr)
                b = nxt - curr*a

        if nums[i]*a + b != nums[i+1]:
            flag = False

    if flag:
        print(nums[-1]*a + b)
    else:
        print('B')
