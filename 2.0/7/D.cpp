#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false), cin.tie(0), cout.tie(0);
    int n, m;
    cin >> n >> m;
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    while(m--) {
        int l, r;
        cin >> l >> r;
        int qty = 0;
        for (int kitten : a) {
            if (kitten >= l && kitten <= r) qty++;
        }
        cout << qty << endl;
    }

    return 0;
}