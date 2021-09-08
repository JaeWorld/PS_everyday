// BOJ 1451. 직사각형으로 나누기

#include <bits/stdc++.h>

using namespace std;

int N, M;
long long ans = 0;
int arr[201][201];

long long calc(int x1, int y1, int x2, int y2) {
    long long ret = 0;
    for (int i=x1; i<=x2; i++) {
        for (int j=y1; j<=y2; j++) {
            ret += arr[i][j];
            //cout << arr[i][j] << endl;
        }
    }

    return ret;
}

int main() {
    cin >> N >> M;
    for (int i=0; i<N; i++) {
        for (int j=0; j<M; j++) {
            char tmp;
            cin >> tmp;
            arr[i][j] = tmp - '0';
        }
    }

    // case1 (ㅏ)
    for (int i=0; i<N-1; i++) {
        for (int j=0; j<M-1; j++) {
            long long area = (calc(0, 0, N-1, j) * calc(0, j+1, i, M-1) * calc(i+1, j+1, N-1, M-1));
            ans = max(ans, area);
            //cout << N-1 << ' ' << j << endl;
        }
    }
    // case2 (ㅓ)
    for (int i=0; i<N-1; i++) {
        for (int j=1; j<=M-1; j++) {
            long long area = (calc(0, 0, i, j-1) * calc(i+1, 0, N-1, j-1) * calc(0, j, N-1, M-1));
            ans = max(ans, area);
        }
    }
    // case3 (ㅗ)
    for (int i=1; i<=N-1; i++) {
        for (int j=0; j<M-1; j++) {
            long long area = (calc(0, 0, i-1, j) * calc(0, j+1, i-1, M-1) * calc(i, 0, N-1, M-1));
            ans = max(ans, area);
        }
    }
    // case4 (ㅜ)
    for (int i=0; i<N-1; i++) {
        for (int j=0; j<M-1; j++) {
            long long area = (calc(0, 0, i, M-1) * calc(i+1, 0, N-1, j) * calc(i+1, j+1, N-1, M-1));
            ans = max(ans, area);
        }
    }
    // case5 (ㅣㅣ)
    for (int i=0; i<M-2; i++) {
        for (int j=i+1; j<M-1; j++) {
            long long area = (calc(0, 0, N-1, i) * calc(0, i+1, N-1, j) * calc(0, j+1, N-1, M-1));
            ans = max(ans, area);
        }

    }
    // case6 (=)
    for (int i=0; i<N-2; i++) {
        for (int j=i+1; j<N-1; j++) {
            long long area = (calc(0, 0, i, M-1) * calc(i+1, 0, j, M-1) * calc(j+1, 0, N-1, M-1));
            ans = max(ans, area);
        }
    }

    cout << ans << endl;
    return 0;
}

