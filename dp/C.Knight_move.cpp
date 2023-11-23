#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;

int main () {
    ios::sync_with_stdio(NULL), cin.tie(0), cin.tie(0);
    freopen("knight.in", "r", stdin);
    freopen("knight.out", "w", stdout);
    int n, m;
    cin >> n >> m;

    vector<vector<int>> dp(n, vector<int>(m));

    dp[0][0] = 1;
    if (m >= 2 && n >= 3) dp[2][1] = 1;
    if (m >= 3 && n >= 2) dp[1][2] = 1;


    for (int i = 2; i < n; i++) {
        for (int j = 2; j < m; j++) {
            dp[i][j] = dp[i - 2][j - 1] + dp[i - 1][j - 2];
        }
    }
    
    cout << dp[n - 1][m - 1] << "\n";


    return 0;
}