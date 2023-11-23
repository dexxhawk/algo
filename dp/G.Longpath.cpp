#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

const int INF = 10001;

int main() {
    ios::sync_with_stdio(false), cin.tie(0), cout.tie(0);
    freopen("longpath.in", "r", stdin);
    freopen("longpath.out", "w", stdout);


    int n, m;
    cin >> n >> m;

    vector<vector<int>> E(n + 1);
    for (int i = 0; i < m; i++) {
        int b, e;
        cin >> b >> e;
        E[b].push_back(e);
    }

    vector<int> dp(n, -INF);
    return 0;
}