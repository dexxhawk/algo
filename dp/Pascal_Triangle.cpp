#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;

int main () {
    ios::sync_with_stdio(NULL), cin.tie(0), cin.tie(0);
    int n, m;
    cin >> n;

    vector<vector<int>> dp(n, vector<int>(n));

    for (int i = 0; i < n; i++) {
        dp[i][0] = 1;
    }

    for (int i = 1; i < n; i++) {
        for (int j = 1; j <= i; j++) {
            dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]; 
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j <= i; j++) {
            cout << dp[i][j] << " ";
        }
        cout << "\n";
    }



    return 0;
}