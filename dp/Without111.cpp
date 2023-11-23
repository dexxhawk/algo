#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;

int main () {
    ios::sync_with_stdio(NULL), cin.tie(0), cin.tie(0);
    int n;
    cin >> n;
    if (n == 1) {
        cout << 2 << "\n";
        return 0;
    }

    long long dp0 = 1, dp1= 2, dp2 = 4;
    long long ans = dp2;
    for (int i = 3; i < n + 1; i++) {
        ans = dp0 + dp1 + dp2;
        dp0 = dp1;
        dp1 = dp2;
        dp2 = ans;
    }

    cout << ans << "\n";

    return 0;
}