# BOJ 1043 거짓말

import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    know = list(map(int, input().split()))
    kn = know.pop(0)
    kl = know
    parties = [list(map(int, input().split())) for _ in range(m)]
    truth = [0]*(n+1)
    ans = 0

    for i in range(kn):
        truth[kl[i]] = 1

    for _ in range(m):
        for party in parties:
            pn = party[0]
            pl = party[1:]
            flag = True
            for i in range(pn):
                if truth[pl[i]] == 1:
                    flag = False
                    break
            if not flag:
                for i in range(pn):
                    truth[pl[i]] = 1

    for party in parties:
        pn = party[0]
        pl = party[1:]
        flag = True
        for i in range(pn):
            if truth[pl[i]] == 1:
                flag = False
                break
        if flag:
            ans += 1

    print(ans)

main()
