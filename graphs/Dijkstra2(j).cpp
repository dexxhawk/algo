#include <bits/stdc++.h>
using namespace std;

int main () {

    const int INF  = 10e4;
    ios::sync_with_stdio(NULL);
    freopen("INPUT.TXT", "r", stdin);
    freopen("OUTPUT.TXT", "w", stdout);

    int n, s, f;
    cin >> n >> s >> f;
    s--, f--;

    vector<vector<int>> mtx(n, vector<int> (n));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> mtx[i][j];
            if (mtx[i][j] == -1) mtx[i][j] = INF;
        }
    }

    vector<int> dist(n, INF);
    vector<int> p(n, s);
    dist[s] = 0;
    set<pair<int, int>> st;
    st.insert({dist[s], s});

    while(!st.empty()) {
        int nearest = st.begin()->second;
        st.erase(st.begin());

        for (int i = 0; i < n; i++) {
            if (dist[i] > dist[nearest] + mtx[nearest][i]) {
                st.erase(pair<int, int> (dist[i], i));
                dist[i] = dist[nearest] + mtx[nearest][i];
                st.insert(pair<int, int> (dist[i], i));
                p[i] = nearest;
            }
        }
    }

    vector<int> ans;

    if (dist[f] == INF) {
        cout << -1;
        return 0;
    }
    

    int v = f; 
    while (v != s) {
        v = p[v];
        ans.push_back(v + 1);
    }

    for (int i = 0; i < ans.size(); i++){
        cout << ans[ans.size() - i - 1] << " ";
    }

    cout << f + 1 << " ";

    return 0;
}