#include <bits/stdc++.h>
using namespace std;

int main() {

    freopen("INPUT.TXT", "r", stdin);
    freopen("OUTPUT.TXT", "w", stdout);

    int n;
    cin >> n;

    vector<vector<int>> mtx (n, vector<int>(n));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> mtx[i][j];
        }
    }

    for (int k = 0; k < n; k++){
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                mtx[i][j] = min(mtx[i][j], mtx[i][k] + mtx[k][j]);
            }
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << mtx[i][j] << " ";
        }
        cout << endl;
    }





    return 0;
}