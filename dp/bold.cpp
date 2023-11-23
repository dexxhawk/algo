#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(NULL), cin.tie(0), cout.tie(0);
    freopen("lepus.in", "r", stdin);
    freopen("lepus.out", "w", stdout);
    int n;
    cin >> n;

    vector<int> a(n + 1);
    for (int i = 1; i < n + 1; i++) {
        char in;
        cin >> in;
        if (in == '"') a[i] = 1;
        else if (in == '.') a[i] = 0;
        else a[i] = -1;
    }

    vector<int> dp(n + 1);

    for (int i = 1; i < n + 1; i++) {
        if (i - 5 > 0 && a[i - 5] < 0 && a[i - 3] < 0 && a[i - 1] < 0) {
            cout << -1;
            return 0;
        }
        if (i - 5 > 0) {
            dp[i] = max(dp[i - 5], max(dp[i - 3], dp[i - 1])) + a[i];
        }
        else if (i - 3 > 0) {
            dp[i] = max(dp[i - 3], dp[i - 1]) + a[i];
        }
        else {
            dp[i] = dp[i - 1] + a[i];
        }
    }

    cout << dp[n];

    return 0;
}