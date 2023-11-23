#include<iostream>
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

int main() {
    freopen("ladder.in", "r", stdin);
    freopen("ladder.out", "w", stdout);
    int n;
    cin >> n;
    vector<int> a(n + 1);

    for (int i = 1; i < n + 1; i++) cin >> a[i];
    vector<int> dp(n + 1, INT_MIN);
    dp[0] = 0;
    dp[1] = a[1];
    for (int i = 2; i < n + 1; i++) {
        dp[i] = max(dp[i - 1], dp[i - 2]) + a[i];
    }

    cout << dp[n] << "\n";

    return 0;
}
