// BOJ 1562 계단 수

#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <cstring>

using namespace std;

int MOD = 1000000000;
int n;
int cache[10][101][1 << 10];

int func(int curr, int length, int check) {
	if (length == n) {
		return check == (1 << 10) - 1 ? 1 : 0;
	}
	int& res = cache[curr][length][check];
	if (res != -1) {
		return res;
	}

	res = 0;
	if (curr - 1 >= 0) {
		res += func(curr - 1, length + 1, check | (1 << (curr - 1)));
	}
	if (curr + 1 <= 9) {
		res += func(curr + 1, length + 1, check | (1 << (curr + 1)));
	}

	res %= MOD;

	return res;
}

int main() {
	cin >> n;
	int ans = 0;

	for (int i = 1; i <= 9; i++) {
		memset(cache, -1, sizeof(cache));
		ans += func(i, 1, 1 << i);
		ans %= MOD;
	}

	cout << ans << endl;
}
