// BOJ 8901. 화학 제품

#include <bits/stdc++.h>

using namespace std;

int T;
int A, B, C;
int AB, BC, CA;


int main() {
    scanf("%d", &T);

    while (T--) {
        scanf("%d %d %d", &A, &B, &C);
        scanf("%d %d %d", &AB, &BC, &CA);

        int ans = 0;
        for (int AB_cnt=0; AB_cnt<=min(A, B); AB_cnt++) {
            int BC_cnt, CA_cnt;
            if (BC >= CA) {
                BC_cnt = min(B-AB_cnt, C);
                CA_cnt = min(A-AB_cnt, C-BC_cnt);
            }
            else if (CA > BC) {
                CA_cnt = min(A-AB_cnt, C);
                BC_cnt = min(B-AB_cnt, C-CA_cnt);
            }

            ans = max(ans, AB*AB_cnt + BC*BC_cnt + CA*CA_cnt);
        }

        printf("%d\n", ans);
    }

}
