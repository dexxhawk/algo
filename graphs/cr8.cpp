#include <bits/stdc++.h>
using namespace std;

vector<int> dfs(int v, vector<vector<int>>& E ,vector<bool>& used, vector<int>& cc) {
    used[v] = true;
    cc.push_back(v);
    // for (int i = 1; i < E[v].size(); i++) {
    //     cout << i << endl;
    //     if (!used[v]) dfs(E[v][i], E, used, cc);
    // }
    for (int to : E[v]) {
        // cout << "TO:";
        if (!used[to]) dfs(to, E, used, cc);
    }


    return cc;
    
}


int main () {
    ios::sync_with_stdio(NULL);
    int n, m;
    cin >> n >> m;
    n++;
    // unordered_set<int> us ();
    vector<vector<int>> E(n);

    while(m--) {
        int u, v;
        cin >> u >> v;
        E[v].push_back(u);
        E[u].push_back(v);
    }

    vector<bool> used(n);
    for (int i = 0; i < n; i++) {
        used[i] = false;
    }

    vector<vector<int>> allcc;

    for (int i = 1; i < n; i++) {
        vector<int> cc;
        if (!used[i]) {
            dfs(i, E, used, cc);
            allcc.push_back(cc);
        }
    }

    cout << allcc.size() << "\n";

    for (vector<int> vec : allcc) {
        cout << vec.size() << "\n";
        for (int i = 0; i < vec.size();i++) cout << vec[i] << " ";
        cout << endl;
    }
    
}