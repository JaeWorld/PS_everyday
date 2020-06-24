// BOJ 1865 웜홀

// 벨만포드

#include <iostream>
#include <stdio.h>
#include <vector>

using namespace std;

int tc, INF = 987654321;

int main() {
	cin >> tc;
	while (tc--) {
		int n, m, w;
		vector<pair<int, int>> g[501];
		int dist[501] = { INF };
		dist[1] = 0;
		bool negCycle = false;

		cin >> n >> m >> w;
		for (int i = 0; i < m; i++) {
			int s, e, t;
			cin >> s >> e >> t;
			g[s].push_back(make_pair(e, t));
			g[e].push_back(make_pair(s, t));
		}
		for (int i = 0; i < w; i++) {
			int s, e, t;
			cin >> s >> e >> t;
			g[s].push_back(make_pair(e, -t));
		}

		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= n; j++) {
				for (auto cur : g[j]) {
					int adj = cur.first;
					int weight = cur.second;

					if (dist[adj] > dist[j] + weight) {
						dist[adj] = dist[j] + weight;
						if (n == i) negCycle = true;
					}
				}
			}
		}
		if (negCycle) cout << "YES" << endl;
		else cout << "NO" << endl;
	}
}
