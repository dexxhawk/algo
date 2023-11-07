#include <bits/stdc++.h>
using namespace std;

int main() {

    freopen("INPUT.TXT", "r", stdin);
    freopen("OUTPUT.TXT", "w", stdout);

    const int mxm = 10e4;

    int n, m;
    cin >> n >> m;

    vector<vector<int>> mtx(n, vector<int> (n));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i == j) mtx[i][j] = 0;
            else mtx[i][j] = mxm;
        }
        cout << endl;
    }

    while (m--) {
        int i, j, w;
        cin >> i >> j >> w;
        i--, j--;
        mtx[i][j] = w;
        mtx[j][i] = w;
    }

    for (int k = 0; k < n; k++) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                mtx[i][j] = min(mtx[i][j], mtx[i][k] + mtx[k][j]);
            }
        }
    }
    
    vector<int> maxweights(n);

    for (int i = 0; i < n; i++) {
        int maxweigth = 0;
        for (int j = 0; j < n; j++){
            if (maxweigth < mtx[i][j]) maxweigth = mtx[i][j];
        }
        maxweights[i] = maxweigth;
    }

    int minweigth = mxm;
    int ans = 0;
    for (int i = 0; i < n; i++) {
        if (maxweights[i] < minweigth) {
            minweigth = maxweights[i];
            ans = i;
        }
    }

    // int minweigths = 10e4;
    // int ans = 0;
    // for (int i = 0; i < n; i++) {
    //     int curweigths = 0;
    //     for (int j = 0; j < n; j++) {
    //         curweigths += mtx[i][j];
    //     }
    //     if (curweigths < minweigths) {
    //         minweigths = curweigths;
    //         ans = i;
    //     }
    // }

    cout << ans + 1 << "\n";




    return 0;
}