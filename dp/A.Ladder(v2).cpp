#include<iostream>
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

int main() {
    ios::sync_with_stdio(NULL), cin.tie(0), cin.tie(0);
    freopen("ladder.in", "r", stdin);
    freopen("ladder.out", "w", stdout);
    int n;
    cin >> n;
    vector<int> a(n + 1);

    for (int i = 1; i < n + 1; i++) cin >> a[i];
    int dp0 = 0;
    int dp1 = a[1];
    int ans = dp1;

    for (int i = 2; i < n + 1; i++) {
        ans = max(dp0, dp1) + a[i];
        dp0 = dp1;
        dp1 = ans;
    }

    cout << ans << "\n";

    return 0;
}
