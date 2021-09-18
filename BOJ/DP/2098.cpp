// BOJ 2098. 외판원 순회
// dp[v][mask] = 현재 v마을에 있고, mask(비트마스크) 마을을 방문하였을 경우, 시작 마을까지의 최소 거리


#include <bits/stdc++.h>

using namespace std;

int N;
int MAX = 987654321;
int dist[16][16];
int dp[16][65537];

// 현재 v마을에 위치해 있고, mask의 마을들을 방문했을때, 최소 거리를 반환
int travel(int v, int mask) {
    // 모든 마을을 방문한 경우, 현재 마을에서 첫 마을까지 경로가 존재하면 dist[v][i],
    // 경로가 존재하지 않을 경우 MAX 반환
    if (mask == (1<<N)-1) {
        if (dist[v][0]) return dist[v][0];
        else return MAX;
    }
    int &ret = dp[v][mask];
    if (ret != -1) return ret;

    ret = MAX;
    for (int i=0; i<N; i++) {
        // 이미 방문한 마을일 경우
        if (mask & (1<<i)) continue;
        // 경로가 존재하지 않을 경우
        if (dist[v][i] == 0) continue;
        ret = min(ret, dist[v][i] + travel(i, mask | (1<<i)));
    }
    return ret;
}


int main() {
    cin >> N;
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            cin >> dist[i][j];
        }
    }

    memset(dp, -1, sizeof(dp));
    int ans = travel(0, 1);
    cout << ans << endl;
}
