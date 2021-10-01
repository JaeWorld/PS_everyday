# BOJ 1082. 방 번호

import sys
input = sys.stdin.readline

# 가격이 같은 경우 큰 숫자만 남긴 리스트 반환
def removeSamePrice(l):
    ret = []
    for i in range(len(l)-1):
        idx, num = l[i]
        nxtidx, nxtnum = l[i+1]
        if (num == nxtnum):
            continue
        else:
            ret.append((idx, num))
    ret.append(l[-1])
    return ret

# prev, new의 각 자리수를 종합하여 가장 큰 수 조합
def comb(prev, new):
    if (prev == 0):
        return new
    ret = list(str(prev))
    ret.append(str(new))
    ret = ''.join(sorted(ret, reverse=True))
    return int(ret)


if __name__ == "__main__":
    N = int(input())
    P = list(map(int, input().split()))
    M = int(input())
    dp = [0]*(M+1)

    P = sorted(list(enumerate(P)), key=lambda x: x[1])
    ret = removeSamePrice(P)

    for i in range(M+1):
        for j in range(len(ret)):
            idx, num = ret[j]
            if (i+num > M):
                continue
            dp[i+num] = max(dp[i+num], comb(dp[i], idx))
    
    print(dp[M])
    
