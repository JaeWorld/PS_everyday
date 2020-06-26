// BOJ 14400 편의점2

#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

int n;
vector<int> X;
vector<int> Y;

int main() {
	long long res = 0;
	cin >> n;
	for (int i=0; i<n; i++) {
		int x, y;
		cin >> x >> y;
		X.push_back(x);
		Y.push_back(y);
	}

	sort(X.begin(), X.end());
	sort(Y.begin(), Y.end());
	
	int cx = X[n / 2];
	int cy = Y[n / 2];

	for (int i = 0; i < n; i++) {
		int temp = abs(cx - X[i]) + abs(cy - Y[i]);
		res += temp;
	}
	cout << res << endl;
}

