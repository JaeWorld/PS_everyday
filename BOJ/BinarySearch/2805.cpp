// BOJ 2805. 나무 자르기

#include <bits/stdc++.h>

using namespace std;

int N, M;
long long ans = 0;
long long arr[1000001];
long long high = pow(10, 9) * 2 + 1;
long long low = 1;

long long calc_meters(int h) {
    long long meters = 0;
    for (int i=0; i<N; i++) {
        if (arr[i] > h) {
            meters += arr[i] - h;
        }
    }
    return meters;
}

void binary() {
    while (low <= high) {
        long long mid = (high + low) / 2;
        long long meters = calc_meters(mid);
        // 필요한 양 이상을 얻은 경우 -> 높이를 높여야함
        if (meters >= M) {
            ans = max(ans, mid);
            low = mid+1;
        }
        // 필요한 양보다 적게 얻은 경우 -> 높이를 낮춰야함
        else {
            high = mid-1;
        }
    }
}

int main() {
    cin >> N >> M;
    for (int i=0; i<N; i++) {
        cin >> arr[i];
    }

    binary();
    cout << ans << endl;

}
