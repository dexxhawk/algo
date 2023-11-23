#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(NULL), cin.tie(0), cout.tie(0);
    int n, s;
    cin >> s >> n;

    vector<int> w(n + 1, 0);
    for (int i = 1; i < n + 1; i++) cin >> w[i];
 
    vector<vector<bool>> dp(n + 1, vector<bool>(s + 1, false));
    dp[0][0] = true;
    for (int i = 1; i < n + 1; i++) {
        for (int j = 0; j < s + 1; j++) {
            dp[i][j] = dp[i - 1][j];
            if (j - w[i] >= 0 && dp[i - 1][j - w[i]]) {
                dp[i][j] = true;
            }
        }
    }

    int ans = 0;
    for (int j = 0; j < s + 1; j++) {
        if (dp[n][j] && ans < j) ans = j;
    }

    cout << ans << endl;

    return 0;
}