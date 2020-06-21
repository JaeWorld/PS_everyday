// BOJ 2630 색종이 만들기

// 재귀

#include <iostream>

using namespace std;

int n, white = 0, blue = 0;
int arr[128][128];

void recursion(int x, int y, int l) {
	int w = 0, b = 0;
	bool flag = true;
	for (int i = x; i < x+l; i++) {
		for (int j = y; j < y+l; j++) {
			if (arr[i][j] == 0) w++;
			if (arr[i][j] == 1) b++;
		}
	}

	if ((w == 0 && b != 0) || (b == 0 && w != 0)) {
		if (w > 0) white++;
		else if (b > 0) blue++;
		return;
	}
	else {
		recursion(x, y, l / 2);
		recursion(x, y + l / 2, l / 2);
		recursion(x + l / 2, y, l / 2);
		recursion(x + l / 2, y + l / 2, l / 2);
	}
}

int main() {
	cin >> n;;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> arr[i][j];
		}
	}
	recursion(0, 0, n);
	cout << white << "\n" << blue << endl;
}
