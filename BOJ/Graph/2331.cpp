#include <bits/stdc++.h>

using namespace std;

const int MAX = 300001;
int A, P;
int visited[MAX] = {0};

int calc_next(int x) {
    int nxt = 0;
    while(x) {
        nxt += (int)floor(pow((x%10), P)+0.5);
        x /= 10;
    }
    return nxt;
}

void dfs(int x) {
    visited[x] += 1;
    if (visited[x] == 3) {
        return;
    }

    int nxt = calc_next(x);
    dfs(nxt);
}

int main() {
    int ans = 0;
    cin >> A >> P;
    dfs(A);

    for (int i=0; i<MAX; i++) {
        if (visited[i] == 1) {
            ans += 1;
        }
    }

    cout << ans << endl;
    return 0;
}
