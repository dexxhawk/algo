#include <iostream>
#include <vector>
#include <iomanip>
#include <algorithm>
using namespace std;

//I think it's much easier to solve the symmetric task
int main () {
    ios::sync_with_stdio(NULL), cin.tie(0), cin.tie(0);
    freopen("king2.in", "r", stdin);
    freopen("king2.out", "w", stdout);
    int n = 8;
    vector<vector<int>> a(n, vector<int>(n));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> a[i][j];
        }
    }

    vector<vector<int>> dp(n, vector<int>(n));
    for (int i = n - 2; i >= 0; i--) {
        dp[i][0] = dp[i + 1][0] + a[i][0];
    }
    for (int j = 1; j < n; j++) {
        dp[n - 1][j] = dp[n - 1][j - 1] + a[n - 1][j];
    }

    for (int i = n - 2; i >= 0; i--) {
        for (int j = 1; j < n; j++) {
            dp[i][j] = min(dp[i + 1][j - 1], min(dp[i + 1][j], dp[i][j - 1])) + a[i][j];
        }
    }

    cout << dp[0][n - 1] << "\n";


    return 0;
}