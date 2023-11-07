#include <bits/stdc++.h>
using namespace std;

int main() {
    const int INF = 1e6;
    ios::sync_with_stdio(NULL);
    freopen("INPUT.TXT", "r", stdin);
    freopen("OUTPUT.TXT", "w", stdout);

    int n, d, v, r;
    cin >> n >> d >> v >> r;
    d--; v--;

    vector<vector<vector<int>>> e(n);

    for (int i = 0; i < r; i++) {
        int from, t_start, to, t_end;
        cin >> from >> t_start >> to >> t_end;
        from--, to--;
        e[from].push_back({to, t_start, t_end});
    }

    vector<int> dist(n, INF);
    dist[d] = 0;
    set<pair<int, int>> st;
    st.insert({dist[d], d});

    while(!st.empty()) {
        int nearest = st.begin()->second;
        st.erase(st.begin());

        for (vector<int>& tp : e[nearest]) {
            int to = tp[0], t_start = tp[1], t_end = tp[2];
            if (dist[nearest] <= t_start && dist[to] > t_end) {
                st.erase({dist[nearest], to});
                dist[to] = t_end;
                st.insert({dist[nearest], to});
            }
        }

    }

    cout <<  (dist[v] ==  INF ? -1 : dist[v]);




    return 0;
}