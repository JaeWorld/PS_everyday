// BOJ 2133. 타일 채우기

#include <bits/stdc++.h>

using namespace std;

int N;
int dp[31];

int main() {
    cin >> N;

    dp[0] = 1;
    dp[2] = 3;

    for (int i=4; i<=N; i++) {
        if (i%2 == 1) continue;

        dp[i] = dp[i-2] * 3;

        for (int j=i-4; j>=0; j-=2) {
            dp[i] += dp[j] * 2;
        }
    }

    cout << dp[N] << endl;

}
