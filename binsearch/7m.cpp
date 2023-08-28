#include <bits/stdc++.h>
using namespace std;



int main () {
    ios::sync_with_stdio(false);

    double c;
    cin >> c;

    double l = 0, r = 1e5;

    for (int i = 0; i < 37; i++){
        double m = (l + r) / 2;
        if (m*m + sqrt(m) >= c) r = m;
        else l = m;
    }

    cout << setprecision(20) << r << "\n";

    return 0;
}