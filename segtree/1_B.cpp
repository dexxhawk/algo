#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

struct segtree {
    vector<int> tree;
    int size;

    void init(int n) {
        size = 1;
        while(size < n) size *= 2;
        tree.assign(2 * size - 1, INT_MAX);
    }

    void build(vector<int>& a, int x, int lx, int rx) {
        if (rx - lx == 1){
            if(lx < a.size()) tree[x] = a[lx];
        }
        else {
            int m = (lx + rx) / 2;
            build(a, 2 * x + 1, lx, m);
            build(a, 2 * x + 2, m, rx);
            tree[x] = min(tree[2 * x + 1], tree[2 * x +  2]);
        }

    }

    void build(vector<int>& a) {
        init(a.size());
        build(a, 0, 0, size);
    }

    void set(int i, int v, int x, int lx, int rx) {
        if (rx - lx == 1){
            tree[x] = v;
            return;
        }

        int m = (lx + rx) / 2;
        if (i < m) {
            set(i, v, 2 * x + 1, lx, m);
        } else {
            set(i, v, 2 * x + 2, m, rx);
        }

        tree[x] = min(tree[2 * x + 1],  tree[2 * x + 2]);
    }

    void set(int i, int v) {
        set(i, v, 0, 0, size);
    }

    int mnm(int l, int r, int x, int lx, int rx) {
        if (lx >= r || rx <= l) {
            return INT_MAX;
        }
        if (lx >= l && rx <= r) {
            return tree[x];
        }
        int m = (lx + rx) / 2;
        int m1 = mnm(l, r , 2 * x + 1, lx, m);
        int m2 = mnm(l, r , 2 * x + 2, m, rx);
        return min(m1, m2);
    }

    int mnm(int l, int r) {
        return mnm(l, r, 0, 0, size);
    }
};


int main () {
    ios::sync_with_stdio(NULL);
    int n, m;
    cin >> n >> m;

    vector<int> a(n);

    for (int i = 0; i < n; i++) cin >> a[i];

    segtree st;
    st.build(a);

    while (m--) {
        int t;
        cin >> t;

        if (t == 1) {
            int i, v;
            cin >> i >> v;
            st.set(i, v);
        } else {
            int l, r;
            cin >> l >> r;
            cout << st.mnm(l, r) << "\n";
        }
    }
}