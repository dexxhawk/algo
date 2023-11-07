#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

class segtree {
    unordered_set<int> NILL;
    vector<unordered_set<int>> tree;
    int size;
    public:

    void combine(int x, unordered_set<int>& s1, unordered_set<int>& s2) {
        tree[x].insert(s1.begin(), s1.end());
        tree[x].insert(s2.begin(), s2.end());
        
    }

    void build(vector<int>& a, int x, int lx, int rx) {
        if (rx - lx == 1) {
            if (lx < a.size()) tree[x].insert(a[lx]);
        }
        else {
            int m = (lx + rx) >> 1;
            build(a, 2 * x + 1, lx, m);
            build(a, 2 * x + 2, m, rx);
            combine(x, tree[2 * x + 1], tree[2 * x + 2]);
        }

    }

    segtree(vector<int>& a) {
        size = 1;
        while(size < a.size()) size *= 2;
        tree.assign(2 * size - 1, {});
        
        build(a, 0, 0, size);
    }

    int set(int i, int v, int x, int lx, int rx) {
        if (rx - lx == 1){
            int del = *tree[x].begin();
            tree[x].erase(del);
            tree[x].insert(v);
            return del;
        }

        int del;
        int m = (lx + rx) >> 1;
        if (i < m) {
            del = set(i, v, 2 * x + 1, lx, m);
        } else {
            del = set(i, v, 2 * x + 2, m, rx);
        }

        if(!(tree[2 * x + 1].count(del) || tree[2 * x + 2].count(del))) {
            tree[x].erase(del);
        } 
        tree[x].insert(v);
        return del;
    }

    void set(int i, int v) {
        set(i, v, 0, 0, size);
    }

    void cnt_unique(int l, int r, int x, int lx, int rx, unordered_set<int>& ans) {
        if (l >= rx || r <= lx) {
            return;
        }

        if (lx >= l && rx <= r){
            ans.insert(tree[x].begin(), tree[x].end());
            return;
        }

        int m = (lx + rx) >> 1;
        cnt_unique(l, r, 2 * x + 1, lx, m, ans);
        cnt_unique(l, r, 2 * x + 2, m, rx, ans);
        return;
    }

    int cnt_unique(int l, int r) {
        unordered_set<int> ans;
        cnt_unique(l, r, 0, 0, size, ans);
        return ans.size();
    }

};


int main () {
    ios::sync_with_stdio(NULL), cin.tie(0), cout.tie(0);
    int n, q;
    cin >> n >> q;
    
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    segtree st(a);

    while(q--) {
        int type;
        cin >> type;
        if(type == 1) {
            int l, r;
            cin >> l >> r;
            l--;
            cout << st.cnt_unique(l, r) << "\n";
        } else {
            int i, v;
            cin >> i >> v;
            i--;
            st.set(i, v);
        }
    }
    return 0;
}