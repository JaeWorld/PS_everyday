// BOJ 1783. 병든 나이트 
// 오른쪽으로만 이동할 수 있다는 점에 유의!!!

#include <bits/stdc++.h>

using namespace std;

int N, M;
int ans;

int main() {
    cin >> N >> M;

    if (N==1) ans = 1;
    else if (N==2) {
        if (M<=2) ans = 1;
        else if(M>=3 & M<5) ans = 2;
        else if (M>=5 & M<=6) ans = 3;
        else ans = 4;
    }
    else if (N>=3) {
        if (M<=4) ans = M;
        else if (M>4 & M<=6) ans = 4;
        else ans = M-2;
    }

    cout << ans << endl;
}

