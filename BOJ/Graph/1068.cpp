// BOJ 1068 트리

// BFS

#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int n, node, d, root, res = 0;
vector<int> v[51];
bool visited[51];

void bfs(int start) {
	queue<int> q;
	visited[start] = true;
	q.push(start);
	
	while (!q.empty()) {
		int curr = q.front();
		q.pop();
		int child = 0;
		for (int i=0; i<v[curr].size(); i++) {
			int nxt = v[curr][i];
			if (!visited[nxt]) {
				child++;
				visited[nxt] = true;
				q.push(nxt);
			}
		}
		if (child == 0) {
			res++;
		}
	}
}

int main()
{
    cin >> n;
    for(int i=0; i<n; i++) {
    	cin >> node;
    	if (node != -1) {
	        v[i].push_back(node);
    	    v[node].push_back(i);
    	} else {
    		root = i;
    	}
    }
    cin >> d;
    visited[d] = true;
    
    if (!visited[root]) {
    	bfs(root);
    }

    cout << res << endl;
}
