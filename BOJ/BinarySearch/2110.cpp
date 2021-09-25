// BOJ 2110. 공유기 설치

#include <bits/stdc++.h>

using namespace std;

int N, C;
long long x[200001];
long long low = 0;
long long high;
long long ans = 0;

// d 이상의 거리 차이로 설치할 수 있는 공유기의 수
int countRouters(int d) {
    int routers = 1;
    int currentRouter = x[0];
    for (int i=1; i<N; i++) {
        if (currentRouter + d <= x[i]) {
            routers++;
            currentRouter = x[i];
        }

    }
    return routers;
}

void binary() {
    long long high = x[N-1] - x[0];
    long long low = 1;
    while (low <= high) {
        long long mid = (low+high) / 2;

        int routers = countRouters(mid);
        // 설치할 수 있는 라우터의 개수가 설치해야하는 라우터 개수 이상일때 -> mid 늘려야
        if (routers >= C) {
            ans = max(ans, mid);
            low = mid+1;
        }
        else if (routers < C) {
            high = mid-1;
        }
    }
}

int main() {
    cin >> N >> C;
    for (int i=0; i<N; i++) {
        cin >> x[i];
        high = max(high, x[i]);
    }

    sort(x, x+N);

    binary();

    cout << ans << endl;

}
