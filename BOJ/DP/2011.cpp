// BOJ 2011. 암호코드

#include <bits/stdc++.h>

using namespace std;

string pw;
int dp[5010];
bool correct = true;


void func() {
    for (int i=2; i<pw.length(); i++) {
        int f = pw[i-1] - '0';
        int b = pw[i] - '0';
        if (b == 0) {
            if (f > 2 | f == 0) correct = false;
            else dp[i] = dp[i-2];
        }
        else if (1 <= b & b <= 6) {
            if (f == 0) dp[i] = dp[i-1];
            else if (f <= 2) dp[i] = dp[i-1] + dp[i-2];
            else dp[i] = dp[i-1];
        }
        else if (b >= 7) {
                if (f >= 2) dp[i] = dp[i-1];
                else if (f == 0) dp[i] = dp[i-1];
                else dp[i] = dp[i-1] + dp[i-2];

        }
        dp[i] = dp[i] % 1000000;
    }
}

int main() {
    cin >> pw;
    int ans;
    memset(dp, 0, sizeof(dp));

    dp[0] = 1;

    int f = pw[0] - '0';
    int b = pw[1] - '0';
    if (f == 0) {
        correct = false;
    }
    if (f != 0 & pw.length() == 1) {
        cout << 1 << endl;
        return 0;
    }

    if (b == 0) {
        if (f > 2 | f == 0) {
            correct = false;
        } else dp[1] = dp[0];
    }
    else if (b >= 1 & b <= 6) {
        if (f != 0 & f <= 2) dp[1] = 2;
        else dp[1] = 1;
    }
    else if (b >= 7) {
        if (f != 0 & f <= 1) dp[1] = 2;
        else dp[1] = 1;
    }

    func();

    if (correct) {
        ans = dp[pw.length() - 1];
    } else {
        ans = 0;
    }
    cout << ans << endl;

    return 0;
}

