#include <iostream>
#include <vector>
#include <iomanip>
#include <algorithm>
using namespace std;

const int INF = 101;

// USE -INF beacause inp can be < 0
int main () {
    ios::sync_with_stdio(NULL), cin.tie(0), cin.tie(0);
    int n;
    cin >> n;

    vector<vector<int>> dp(n, vector<int>(n, -INF));
    cin >> dp[0][0];
    for (int i = 1; i < n; i++) {
        for (int j = 0; j <= i; j++) {
            int inp;
            cin >> inp;
            if (j == 0) {
                dp[i][j] = dp[i - 1][j] + inp;
            }
            else {
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + inp;
            }

        }
    }

    cout << *max_element(dp.back().begin(), dp.back().end()) << "\n";

    return 0;
}