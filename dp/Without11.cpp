#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;

int main () {
    ios::sync_with_stdio(NULL), cin.tie(0), cin.tie(0);
    int n;
    cin >> n;

    double dp0 = 1, dp1= 2, ans = dp1;
    for (int i = 2; i < n + 1; i++) {
        ans = dp0 + dp1;
        dp0 = dp1;
        dp1 = ans;
    }

    cout << fixed << setprecision(0) << ans << "\n";

    return 0;
}