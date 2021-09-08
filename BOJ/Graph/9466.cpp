// BOJ 9466. 텀 프로젝트
// dfs로 탐색하면서 사이클이 있는 경우, 사이클의 요소 개수를 카운트.

#include <bits/stdc++.h>

using namespace std;


int T, n, cnt;
int visited[100001];
int finished[100001];
int s[100001];

void dfs(int x) {
    visited[x] = 1;

    int nxt = s[x];
    if (!visited[nxt]) {
        dfs(nxt);
    } else {
        if (!finished[nxt]) {
            for (int i=nxt; i!=x; i=s[i]) {
                cnt++;
            }
            cnt++;
        }
    }
    finished[x] = 1;
}

int main() {
    cin >> T;

    while (T--) {
        cin >> n;
        for (int i=1; i<=n; i++) {
            cin >> s[i];
        }

        memset(visited, 0, sizeof(visited));
        memset(finished, 0, sizeof(finished));

        cnt = 0;
        for (int i=1; i<=n; i++) {
            if (!visited[i]) {
                dfs(i);
            }
        }

        cout << n-cnt << endl;
    }

}
