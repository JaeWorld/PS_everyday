// BOJ 5635 생일

#include <iostream>
#include <algorithm>

using namespace std;

struct Student {
  string name;
  int d, m, y;
};

int n;
Student s[100];

bool cmp(Student &a, Student &b) {
  if (a.y != b.y) return a.y > b.y;
  else if (a.m != b.m) return a.m > b.m;
  else if (a.d != b.d) return a.d > b.d;
}

int main() {
  cin >> n;
  for (int i=0; i<n; i++) {
    cin >> s[i].name >> s[i].d >> s[i].m >> s[i].y;
  }
  sort(s, s+n, cmp);
  cout << s[0].name << '\n' << s[n-1].name << endl;
  return 0;
}
