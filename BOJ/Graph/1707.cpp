// BOJ 1707. 이분 그래프
// 인접한 노드에 다른 색을 칠하면서 인접한 노드의 색을 확인.
// 만약 인접한 노드에 이미 같은 색일 칠해져 있다면, 이분 그래프 불가능.

#include <bits/stdc++.h>

using namespace std;

int K;
vector<int> graph[20001];
int visited[20001];
bool correct = true;

void dfs(int x, int color) {
    visited[x] = color;

    for (int i=0; i<graph[x].size(); i++) {
        int nxt = graph[x][i];
        if (visited[nxt] == 0) {
            dfs(nxt, 3-color);
        } else if (visited[nxt] == color) {
            correct = false;
            return;
        }
    }
}

int main() {
    cin >> K;
    while (K--) {
        int V, E;
        string ans;
        cin >> V >> E;

        for (int i=0; i<E; i++) {
            int u, v;
            cin >> u >> v;
            graph[u].push_back(v);
            graph[v].push_back(u);
        }
        memset(visited, 0, sizeof(visited));
        correct = true;

        for (int i=1; i<=V; i++) {
            if (visited[i] == 0)
                dfs(i, 1);
        }

        ans = correct ? "YES" : "NO";
        cout << ans << endl;

        // clear graph, visited
        for (int i=1; i<=V; i++) {
            graph[i].clear();
            visited[i] = 0;
        }

    }
}
