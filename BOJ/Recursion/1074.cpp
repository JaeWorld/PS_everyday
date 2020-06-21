#include <iostream>
#include <math.h>

using namespace std;

int n, r, c;
int res = 0;

void func(int x, int y, int l) {
	if (x == r && y == c) {
		cout << res << endl;
		return;
	}
	if (l == 1) {
		res++;
		return;
	}
	if (!(x <= r && r < x + l && y <= c && c < y + l)) {
		res += l * l;
		return;
	}

	func(x, y, l / 2);
	func(x, y + l / 2, l / 2);
	func(x + l / 2, y, l / 2);
	func(x + l / 2, y + l / 2, l / 2);
}

int main() {
	cin >> n >> r >> c;
	func(0, 0, pow(2, n));
}
