#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;

#define MAX 1000001

int main () {
    ios::sync_with_stdio(NULL), cin.tie(0), cin.tie(0);
    int n;
    cin >> n;

    vector<int> dp(n + 1, MAX);
    dp[1] = 0;

    for (int i = 2; i < n + 1; i++) {
        if (i % 6 == 0) dp[i] = min(dp[i - 1], min(dp[i / 2], dp[i / 3])) + 1;
        else if (i % 3 == 0 ) dp[i] = min(dp[i - 1], dp[i / 3]) + 1;
        else if (i % 2 == 0 ) dp[i] = min(dp[i - 1], dp[i / 2]) + 1;
        else dp[i] = dp[i - 1] + 1;
    }

    cout << dp[n] << "\n";

    return 0;
}