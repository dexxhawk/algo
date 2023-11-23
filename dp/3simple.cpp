#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
typedef long long ll;

const int MOD = 1000000009;

ll dp[10001][10][10];


bool is_prime(int x) {
    for (int i = 2; i * i <= x; i++) {
        if (x % i == 0) return false;
    }
    return true;
}

int main() {
    ios::sync_with_stdio(false), cin.tie(0), cout.tie(0);
    freopen("INPUT.TXT", "r", stdin);
    freopen("OUTPUT.TXT", "w", stdout);
    int n;
    cin >> n;


    // vector<vector<vector<ll>>> dp(n + 1, vector<vector<ll>>(10, vector<ll>(10)));

    vector<int> a(1000, 0);
    for (int i = 0; i < 1000; i++) {
        a[i] = is_prime(i);
    }

    for (int i = 1; i <= 9; i++) {
        for (int j = 0; j <= 9; j++) {
            for (int k = 0; k <= 9; k++) {
                if (a[i * 100 + j * 10 + k]) dp[3][j][k]++;
            }
        }
    }

    for (int l = 4; l <= n; l++) {
        for (int i = 1; i <= 9; i++) {
            for (int j = 0; j <= 9; j++){
                for (int k = 0; k <= 9; k++) {
                    if (a[i * 100 + j * 10 + k]) {
                        dp[l][j][k] = (dp[l][j][k] + dp[l - 1][i][j]) % MOD;
                    }
                }
            }
        }
    }
    ll ans = 0;
    for (int i = 0; i <= 9; i++) {
        for (int j = 0; j <= 9; j++) {
            ans = (ans + dp[n][i][j]) % MOD;
        }
    }

    cout << ans << "\n";
    return 0;
}