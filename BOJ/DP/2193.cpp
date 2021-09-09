// BOJ 2193. 이친수 
// 규칙을 찾아보는 습관!

#include <bits/stdc++.h>

using namespace std;

int N;
long long dp[101];


int main() {
    cin >> N;
    memset(dp, -1, sizeof(dp));
    dp[1] = 1;
    dp[2] = 1;

    for (int i=3; i<=N; i++) {
        dp[i] = dp[i-1] + dp[i-2];
    }

    cout << dp[N] << endl;
    return 0;
}

