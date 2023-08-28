#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

bool ok (vector<ll>& a, int k, ll councilsqty) {
    ll totalqty = 0;
    for (int i = 0; i < a.size(); i++){
        totalqty += min(a[i], councilsqty);
    }
    return totalqty >= k * councilsqty;
}

int main () {
    ios::sync_with_stdio(false);

    int k, n;
    cin >> k >> n;

    vector<ll> a(n);

    for (int i = 0; i < n; i ++) cin >> a[i];

    ll l = 0, r = 1e9 * 25 + 1; // k>=2 => в 1 студсовете минимум 2 человека - лучший расклад
    while (r > l + 1) {
        ll m = (r + l) / 2;
        if (ok(a, k, m)) l = m;
        else r = m;
    }


    cout << l << "\n";

    return 0;
}