#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

#define INF 10000000
#define MAX_TIME 1440
#define CUP_W 100
#define VAN_W 3000000


bool ok (vector<vector<vector<ll>>>& e, ll m) {
    ll cur_w = VAN_W + m * CUP_W;
    int s = 0;
    vector<int> dist(e.size(), INF);
    dist[s] = 0;
    set<pair<int, int>> st;
    st.insert({dist[s], s});

    while(!st.empty()) {
        int nearest = st.begin()->second;
        st.erase(st.begin());

        for (vector<ll>& tp : e[nearest]) {
            ll to = tp[0], time = tp[1], max_w = tp[2];

            if (dist[to] > dist[nearest] + time && cur_w <= max_w) {
                st.erase({dist[to], to});
                dist[to] = dist[nearest] + time;
                st.insert({dist[to], to});
            }
        }

    }
    return dist[e.size() - 1] <= MAX_TIME;
}


int main() {
    

    ios::sync_with_stdio(NULL);
    freopen("INPUT.TXT", "r", stdin);
    freopen("OUTPUT.TXT", "w", stdout);

    int n, m;
    cin >> n >> m;

    vector<vector<vector<ll>>> e(n);

    for (int i = 0; i < m; i++) {
        int from, to, time, max_w;
        cin >> from >> to >> time >> max_w;
        from--, to--;
        e[from].push_back({to, time, max_w});
        e[to].push_back({from, time, max_w});
    }

    //Use binsearch:
    int l = 0, r = 1e7 + 1;

    while (r > l + 1) {
        ll m = (l + r) / 2;
        if (ok(e, m)) l = m;
        else r = m;
    }

    cout << l;

    return 0;
}