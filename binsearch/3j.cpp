#include <bits/stdc++.h>
using namespace std;

int find_upper(int x, vector<int>& a){
    int l = -1;
    int r = a.size();

    while (r > l + 1) {
        int m = (l + r) / 2;
        if (a[m] >= x) {
            r = m;
        } else {
            l = m;
        }
    }
    return r;

}

int main() {
    ios::sync_with_stdio(NULL), cin.tie(0), cout.tie(0);

    int n, k;
    cin >> n >> k;
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    while(k--) {
        int x;
        cin >> x;
        cout << find_upper(x, a) + 1 << endl;
    }

    return 0;

}

