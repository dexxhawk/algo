#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;

int main () {
    ios::sync_with_stdio(NULL), cin.tie(0), cin.tie(0);
    int n, m;
    cin >> n >> m;

    vector<vector<int>> dp(n, vector<int>(m));

    dp[0][0] = 1;
    for (int i = 0; i < n; i++) {
        dp[i][0] = dp[0][0]; 
    }
    for (int j = 0; j < m; j++) {
        dp[0][j] = dp[0][0]; 
    }

    for (int i = 1; i < n; i++) {
        for (int j = 1; j < m; j++) {
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j]; 
        }
    }

    cout << dp[n - 1][m - 1] << "\n";


    return 0;
}