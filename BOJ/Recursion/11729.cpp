// BOJ 11729. 하노이 탑 이동 순서 

#include <bits/stdc++.h>
#include <cstdio>

using namespace std;

int N;
int cnt = 0;
vector<pair<int, int>> proc;

void hanoi(int n, int from, int via, int to) {
    if (n == 0) return;
    hanoi(n-1, from, to, via);
    proc.push_back(make_pair(from, to));
    cnt++;
    hanoi(n-1, via, from, to);
}

int main() {
    scanf("%d", &N);
    hanoi(N, 1, 2, 3);
    printf("%d\n", cnt);
    for (int i=0; i<proc.size(); i++) {
        printf("%d %d\n", proc[i].first, proc[i].second);
    }
    return 0;
}
