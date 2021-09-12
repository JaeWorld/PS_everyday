// BOJ 1707. 이분 그래프
// BFS 사용

#include <bits/stdc++.h>

using namespace std;

int K;
vector<int> graph[20001];
int visited[20001];
int correct = true;


void bfs(int x, int color) {
    queue<pair<int, int>> q;
    q.push(make_pair(x, color));
    visited[x] = color;

    while (!q.empty()) {
        int v = q.front().first;
        int color = q.front().second;
        q.pop();

        for (int i=0; i<graph[v].size(); i++) {
            int nxt = graph[v][i];
            if (visited[nxt] == 0) {
                q.push(make_pair(nxt, 3-color));
                visited[nxt] = 3-color;
            }
            else if (visited[nxt] == color) {
                correct = false;
                return;
            }
        }
    }
}

int main() {
    cin >> K;
    int V, E;
    while (K--) {
        cin >> V >> E;
        int u, v;
        for (int i=0; i<E; i++) {
            cin >> u >> v;
            graph[u].push_back(v);
            graph[v].push_back(u);
        }
        memset(visited, 0, sizeof(visited));

        string ans;
        for (int i=1; i<=V; i++) {
            if (visited[i] == 0) {
                bfs(i, 1);
            }
            if (!correct) break;
        }

        ans = correct ? "YES" : "NO";
        cout << ans << endl;

        for (int i=0; i<=V; i++) {
            graph[i].clear();
        }
        correct = true;

    }

    return 0;
}

