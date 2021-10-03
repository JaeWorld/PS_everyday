// BOJ 2659. 십자카드 문제 

#include <bits/stdc++.h>

using namespace std;

int arr[4];
int clockNum = 10000;
int ans;

bool check(int num) {
    int digits[4];
    int div = 1000;
    for (int i=0; i<4; i++) {
        digits[i] = num/div;
        num %= div;
        div /= 10;
        if (digits[i] == 0) return false;
    }

    int first = digits[0];

    for (int i=1; i<4; i++) {
        if (first > digits[i]) return false;
        if (first == digits[i] && i==3) {
            if (digits[2] != digits[3]) return false;
        }
        if (first == digits[i] && i==2) {
            if (digits[3] < digits[1]) return false;
        }
    }
    return true;
}

int main() {
    for (int i=0; i<4; i++) {
        cin >> arr[i];
    }

    for (int i=0; i<4; i++) {
        int temp = arr[i]*1000 + arr[(i+1)%4]*100 + arr[(i+2)%4]*10 + arr[(i+3)%4];
        clockNum = min(clockNum, temp);
    }

    for (int i=1111; i<=clockNum; i++) {
        if (check(i)) {
            ans++;
        }
    }

    cout << ans << endl;
}
