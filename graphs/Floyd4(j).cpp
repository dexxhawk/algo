#include <bits/stdc++.h>
using namespace std;

int main() {

    freopen("INPUT.TXT", "r", stdin);
    freopen("OUTPUT.TXT", "w", stdout);

    int n, s, t;
    cin >> n >> s >> t;
    t--; s--;

    vector<vector<int>> mtx (n, vector<int>(n));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> mtx[i][j];
            if (mtx[i][j] == -1) mtx[i][j] = 50e6 + 1;
        }
    }

    for (int k = 0; k < n; k++){
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                mtx[i][j] = min(mtx[i][j], mtx[i][k] + mtx[k][j]);
            }
        }
    }

    if (mtx[s][t] != 50e6 + 1)  cout << mtx[s][t] << "\n";
    else cout << -1 << "\n";

    return 0;
}