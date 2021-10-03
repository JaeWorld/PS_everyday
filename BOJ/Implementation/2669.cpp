// BOJ 2669. 직사각형 네개의 합집합의 면적 구하기

#include <bits/stdc++.h>

using namespace std;

int arr[4][4];
int board[101][101];
int ans = 0;

int main() {
    for (int i=0; i<4; i++) {
        for (int j=0; j<4; j++) {
            cin >> arr[i][j];
        }
    }

    memset(board, 0, sizeof(board));

    for (int i=0; i<4; i++) {
        int x1=arr[i][0], y1=arr[i][1];
        int x2=arr[i][2], y2=arr[i][3];
        for (int x=x1+1; x<=x2; x++) {
            for (int y=y1+1; y<=y2; y++) {
                board[y][x] = 1;
            }
        }
    }

    for (int i=0; i<101; i++) {
        for (int j=0; j<101; j++) {
            if (board[i][j] == 1) {
                ans++;
            }
        }
    }

    cout << ans << endl;
}
