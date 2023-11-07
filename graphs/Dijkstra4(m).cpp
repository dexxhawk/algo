#include <bits/stdc++.h>
using namespace std;
 
int main () {
 
    const int INF  = 2009000999 ;
    ios::sync_with_stdio(NULL);
    freopen("INPUT.TXT", "r", stdin);
    freopen("OUTPUT.TXT", "w", stdout);
 
    int n;
    cin >> n;
    vector<int> price(n);
    for (int i = 0; i < n; i++) cin >> price[i];
 
    int m;
    cin >> m;
 
    vector<vector<pair<int, int>>> E(n);
 
    for (int i = 0; i < m; i++) {
        int v, u;
        cin >> v >> u;
        v--, u--;
        E[v].push_back({u, price[v]});
        E[u].push_back({v, price[u]});
    }
 
    vector<int> dist(n, INF);
    set<pair<int, int>> st;
    int s = 0;
 
    dist[s] = 0;
    st.insert({dist[s], s});
 
    while (!st.empty()) {
        int nearest = st.begin() -> second;
        st.erase(st.begin());
 
        for (pair<int, int>& pr : E[nearest]) {
            int to = pr.first, w = pr.second;
            if (dist[to] > dist[nearest] + w) {
                st.erase({dist[to], to});
                dist[to] = dist[nearest] + w;
                st.insert({dist[to], to});
            }
        }
    }
 
    cout << (dist[n-1] == INF ? -1 : dist[n-1]);
 
    return 0;
}