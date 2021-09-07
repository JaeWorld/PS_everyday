// BOJ 1654. 랜선 자르기
// long long을 사용하여 overflow 방지해줘야함.


#include <bits/stdc++.h>
#define LL long long

using namespace std;


int K, N;
LL ans;
int arr[10001];

int cut(int lan, int unit) {
    LL ret = 0;
    while (lan >= unit) {
        lan -= unit;
        ret++;
    }
    return ret;
}

int main() {
    cin >> K >> N;
    for (int i=0; i<K; i++) {
        cin >> arr[i];
    }

    LL left = 1;
    LL right = *max_element(arr, arr+K);

    while (left <= right) {
        LL mid = (left+right)/2;
        LL pieces_cnt = 0;
        for (int i=0; i<K; i++) {
            pieces_cnt += cut(arr[i], mid);
        }
        if (pieces_cnt >= N) {
            ans = max(ans, mid);
            left = mid+1;
        }
        else if (pieces_cnt < N) {
            right = mid-1;
        }
    }

    cout << ans << endl;
}
