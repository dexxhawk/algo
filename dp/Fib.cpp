#include <iostream>
#include <vector>
using namespace std;

int main () {
    ios::sync_with_stdio(NULL), cin.tie(0), cin.tie(0);
    freopen("INPUT.TXT", "r", stdin);
    freopen("OUTPUT.TXT", "w", stdout);
    int n;
    cin >> n;

    int dp0 = 1, dp1= 1, ans = 1;
    for (int i = 2; i < n + 1; i++) {
        ans = (dp0 + dp1) % 10;
        dp0 = dp1;
        dp1 = ans;
    }

    cout << ans << "\n";

    return 0;
}