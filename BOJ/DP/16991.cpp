// BOJ 16991. 외판원 순회 3
// 소수점 자리수 출력 주의!!!

#include <bits/stdc++.h>

using namespace std;

int N;
int start = 0;
double MAX = 987654321;
double dist[20][20];
double dp[20][70000];
int pos[16][2];

double calc_dist(int x1, int y1, int x2, int y2) {
    return sqrt(pow(x1-x2, 2) + pow(y1-y2, 2));
}

double travel(int curr, int visited) {
    double &ret = dp[curr][visited];
    if (ret != -1.0) {
            return ret;
    }

    if (visited == (1<<N)-1) {
        if (dist[curr][start] == 0.0)
            return ret = MAX;
        return ret = dist[curr][start];
    }

    ret = MAX;
    for (int i=0; i<N; i++) {
        if (visited & (1<<i) || dist[curr][i] == 0.0) continue;
        ret = min(ret, dist[curr][i] + travel(i, visited | (1<<i)));
    }
    return ret;
}

int main() {
    cin >> N;
    for (int i=0; i<N; i++) {
        cin >> pos[i][0] >> pos[i][1];
    }

    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            dist[i][j] = calc_dist(pos[i][0], pos[i][1], pos[j][0], pos[j][1]);
        }
    }

    for (int i=0; i<20; i++) {
        for (int j=0; j<(1<<16); j++) {
            dp[i][j] = -1.0;
        }
    }

    printf("%lf", travel(0, 1));
}
