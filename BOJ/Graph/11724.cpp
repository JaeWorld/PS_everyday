#include <bits/stdc++.h>

using namespace std;

int N, M;
vector<int> graph[1001];
int visited[1001];


void bfs(int start) {
    queue<int> q;
    q.push(start);
    visited[start] = 1;

    while(!q.empty()) {
        int x = q.front();
        q.pop();
        for (int i=0; i<graph[x].size(); i++) {
            int nxt = graph[x][i];
            if (!visited[nxt]) {
                q.push(nxt);
                visited[nxt] = 1;
            }
        }
    }
}


int main() {
    cin >> N >> M;
    int u, v;
    int ans = 0;
    for (int i=0; i<M; i++) {
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    for (int i=1; i<=N; i++) {
        if (!visited[i]) {
            bfs(i);
            ans++;
        }
    }

    cout << ans << endl;
    return 0;
}
