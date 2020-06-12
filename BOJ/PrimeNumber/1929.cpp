// BOJ 1929 소수 구하기

// 에라토스테네스의 체

#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

int m, n, nums[1000000] = {0};

int main() {
  cin >> m >> n;

  nums[1] = 1;
  for (int i=2; i<=sqrt(n); i++) {
    for (int j=i*2; j<=n; j+=i) {
      nums[j] = 1;
    }
  }
  for (int i=m; i<=n; i++) {
    if (nums[i] != 1) {
      cout << i << '\n';
    }
  }
  return 0;
}
