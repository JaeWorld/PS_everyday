// BOJ 8895. 막대 배치

// dp[n][l][r] = n개의 막대를 배치하여 왼쪽에 l개, 오른쪽에 r개가 보이는 경우의 수
// 높은 막대부터 내림차순으로 차례로 배치. 낮은 막대가 어디 배치되느냐에 따라 보이는 개수가 달라짐.
// 새로운 막대는 맨 왼쪽/오른쪽/중간 중 하나에 배치 가능.
// 왼쪽: 1가지, 오른쪽: 1가지, 중간: n-2가지 위치에 배치 가능.

#include <bits/stdc++.h>

using namespace std;

int T;
int n, l, r;
long long dp[21][21][21];


int main() {
    scanf("%d", &T);
    while (T--) {
        scanf("%d %d %d", &n, &l, &r);

        memset(dp, 0, sizeof(dp));

        dp[1][1][1] = 1;
        for (int i=2; i<=n; i++) {
            for (int j=1; j<=i; j++) {
                for (int k=1; k<=i; k++) {
                    dp[i][j][k] = dp[i-1][j-1][k] + dp[i-1][j][k-1] + (i-2)*dp[i-1][j][k];
                }
            }
        }

        printf("%lld\n", dp[n][l][r]);

    }
}
