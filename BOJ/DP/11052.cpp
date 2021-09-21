// BOJ 11052. 카드 구매하기

#include <bits/stdc++.h>

using namespace std;

int N;
int arr[1005], dp[1005];


int main() {
    cin >> N;
    for (int i=1; i<=N; i++) {
        cin >> arr[i];
    }

    for (int i=1; i<=N; i++) {
        for (int j=1; j<=i; j++) {
            dp[i] = max(dp[i], dp[i-j] + arr[j]);
        }
    }

    cout << dp[N] << endl;
}
