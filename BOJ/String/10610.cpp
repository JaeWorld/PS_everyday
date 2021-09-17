// BOJ 10610. 30 
// 3의 배수가 되는 조건 = 모든 자리 수의 합이 3의 배수

#include <bits/stdc++.h>

using namespace std;

string N;
vector<int> arr;
int digitSum = 0;
bool hasZero = false;


int main() {
    cin >> N;
    string ans;

    for (int i=0; i<N.size(); i++) {
        int num = N[i] - '0';
        arr.push_back(num);
        digitSum += num;
        if (num == 0) hasZero = true;
    }

    if (!hasZero | (digitSum%3 != 0)) {
        cout << -1 << endl;
        return 0;
    }

    int arr_size = arr.size();
    sort(arr.begin(), arr.end());
    reverse(arr.begin(), arr.end())
;

    for (int i=0; i<arr_size; i++) {
        ans += arr[i] + '0';
    }


    cout << ans << endl;

}

