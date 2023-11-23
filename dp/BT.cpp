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

    vector<int> a(n);
    string s;
    cin >> s;
    for (int i = 0; i < n; ++i) {
        if (s[i] == 'w') {
            a[i] = -1;
        } else if (s[i] == '\"') {
            a[i] = 1;
        }
    }
//    for (int i = 0; i < n; ++i) {
//       cout << a[i] << " ";
//    }
//    cout << endl;
    vector<int> dp(n, -1);
    dp[0] = 0;

    for (int i = 1; i < n; i++) {
    
        if (a[i] < 0) continue;

        if (i - 5 >= 0 && dp[i - 5] >= 0) {
            dp[i] = dp[i - 5] + a[i];
        }
        if (i - 3 >= 0 && dp[i - 3] >= 0) {
            dp[i] = max(dp[i - 3] + a[i], dp[i]);
        }
        if (i - 1 >= 0 && dp[i - 1] >= 0) {
            dp[i] = max(dp[i - 1] + a[i], dp[i]);  
        }
    }
   for (int i = 0; i < n; ++i) {
       cout << dp[i] << " ";
   }
   cout << endl;
    cout << dp[n - 1];

    return 0;
}   