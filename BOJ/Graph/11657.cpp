// BOJ 11657 타임머신

// 벨만포드

#include <iostream>
#include <stdio.h>
#include <vector>

using namespace std;

int n, m, INF = 987654321;
long long dist[501];
bool negCycle = false;
vector<pair<int, int>> g[501];

int main() {
	cin >> n >> m;
	while (m--) {
		int a, b, c;
		cin >> a >> b >> c;
		g[a].push_back(make_pair(b, c));
	}

	for (int i = 1; i <= n; i++) {
		dist[i] = INF;
	}
	dist[1] = 0;

	for (int t = 1; t <= n; t++) {
		for (int i = 1; i <= n; i++) {
			for (int j = 0; j < g[i].size(); j++) {
				int adj = g[i][j].first;
				int weight = g[i][j].second;

				if (dist[i] != INF && dist[adj] > dist[i] + weight) {
					dist[adj] = dist[i] + weight;
					if (t == n) negCycle = true;
				}
			}
		}
	}	

	if (negCycle) {
		cout << -1 << endl;
	}
	else {
		for (int i = 2; i <= n; i++) {
			if (dist[i] != INF) cout << dist[i] << endl;
			else cout << -1 << endl;
		}
	}
}
