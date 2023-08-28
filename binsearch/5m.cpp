#include <bits/stdc++.h>
using namespace std;

int main () {
    ios::sync_with_stdio(false);

    int n, k;
    cin >> n >> k;
    vector<int> a(n);

    for (int i = 0; i < n; i++) cin >> a[i];


    double l = 0, r = 1e7 + 1;
    
    for (int i = 0; i < 44; i++){
        double m = (r + l) * .5;
        int s = 0;
        for (int j = 0; j < n; j++) s += (int)(a[j] / m);

        if (s >= k) l = m;
        else r = m;

    }

    cout << setprecision(20) << l << "\n";

    return 0;
}