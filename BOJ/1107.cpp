// BOJ 1107. 리모컨

#include <bits/stdc++.h>

using namespace std;

int N, M;
vector<int> broken;

int check(int x) {
    int ret = 0;
    if (x == 0) {
        if (find(broken.begin(), broken.end(), x) != broken.end()) return -1;
        else return 1;
    }
    while(x>0) {
        int digit = x%10;
        x /= 10;
        ret++;
        if (find(broken.begin(), broken.end(), digit) != broken.end()) {
            return -1;
        }
    }
    return ret;
}

int main() {
    cin >> N;
    cin >> M;
    for (int i=0; i<M; i++) {
        int b;
        cin >> b;
        broken.push_back(b);
    }

    int ans = abs(100-N);
    for (int i=0; i<=pow(10, 6)+1; i++) {
        int nod = check(i);
        if (nod != -1) {
            //cout << i << ' ' << nod+abs(N-i) << endl;
            ans = min(ans, nod+abs(N-i));
        }
    }

    cout << ans << endl;
}
