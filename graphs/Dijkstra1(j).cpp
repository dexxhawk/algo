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
    // vector<bool> used(n, false);
    dist[s] = 0;
    // used[s] = true;
    set<pair<int, int>> st;
    st.insert({dist[s], s});
 
    while(!st.empty()) {
        int nearest = st.begin()->second;
        st.erase(st.begin());
 
        for (int i = 0; i < n; i++) {
            // if(used[i]) continue;
            if (dist[i] > dist[nearest] + mtx[nearest][i]) {
                st.erase(pair<int, int> (dist[i], i));
                dist[i] = dist[nearest] + mtx[nearest][i];
                st.insert(pair<int, int> (dist[i], i));
            }
        }
    }
 
    dist[f] == INF ? cout << -1 : cout << dist[f];
 
 
    return 0;
}