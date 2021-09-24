// BOJ 1041. 주사위
#include <bits/stdc++.h>

using namespace std;

using LL = long long;

int N;
long long ans = 0;
int arr[7];
int case1=9999, case2=9999, case3=9999;


int main() {
    cin >> N;
    for (int i=0; i<6; i++) {
        cin >> arr[i];
    }

    if (N == 1) {
        for (int i=0; i<6; i++) {
            ans += arr[i];
        }
        ans -= *max_element(arr, arr+6);
        cout << ans << endl;
        return 0;
    }

    case1 = *min_element(arr, arr+6);

    for (int i=0; i<6; i++) {
        for (int j=i+1; j<6; j++) {
            if (5-i == j | i == j) continue;
            case2 = min(case2, arr[i]+arr[j]);
            for (int k=j+1; k<6; k++) {
                if (5-i == k | 5-j == k) continue;
                case3 = min(case3, arr[i]+arr[j]+arr[k]);
            }
        }
    }


    ans += (5*(long long)N*N - 16*N +12) * case1;
    ans += (8*N - 12) * case2;
    ans += 4 * case3;

    cout << ans << endl;

}
