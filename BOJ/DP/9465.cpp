// BOJ 9465. 스티커

#include <bits/stdc++.h>

using namespace std;

int T, n;
int dp[2][100001];
int score[2][100001];

void func() {
    for (int i=1; i<n; i++) {
        dp[0][i] = max(dp[1][i-1]+score[0][i], dp[0][i-1]);
        dp[1][i] = max(dp[0][i-1]+score[1][i], dp[1][i-1]);
    }
}

int main() {
    cin >> T;
    while (T--) {
        memset(score, 0, sizeof(score));
        memset(dp, -1, sizeof(dp));
        cin >> n;
        for (int i=0; i<2; i++) {
            for (int j=0; j<n; j++) {
                cin >> score[i][j];
            }
        }
        dp[0][0] = score[0][0];
        dp[1][0] = score[1][0];

        func();

        int ans = max(dp[0][n-1], dp[1][n-1]);

        cout << ans << endl;
    }
    return 0;
}

