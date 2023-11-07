#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

class segtree {
    vector<ll> tree;
    int size;
    public:

    segtree(int n) {
        size = 1;
        while(size < n) size *= 2;
        tree.assign(2 * size - 1, 0);
    }

    void add(int i, int v, int x, int lx, int rx) {
        if (rx - lx == 1){
            tree[x] += v;
            return;
        }

        int m = (lx + rx) >> 1;
        if (i < m) {
            add(i, v, 2 * x + 1, lx, m);
        } else {
            add(i, v, 2 * x + 2, m, rx);
        }

        tree[x] = tree[2 * x + 1] + tree[2 * x + 2];
    }

    void add(int i, int v) {
        add(i, v, 0, 0, size);
    }

    ll sum(int l, int r, int x, int lx, int rx) {
        if (l >= rx || r <= lx) {
            return 0;
        }

        if (lx >= l && rx <= r){
            return tree[x];
        }

        int m = (lx + rx) >> 1;
        ll s1 = sum(l, r, 2 * x + 1, lx, m);
        ll s2 = sum(l, r, 2 * x + 2, m, rx);

        return s1 + s2;


    }

    ll sum(int l, int r) {
        return sum(l, r, 0, 0, size);
    }
};


int main () {
    ios::sync_with_stdio(NULL), cin.tie(0), cout.tie(0);
    int n, m;
    cin >> n >> m;

    segtree st(n);

    while(m--) {
        int type;
        cin >> type;
        if(type == 1) {
            int l, r, v;
            cin >> l >> r >> v;
            st.add(l, v);
            if (r < n) st.add(r, -v);
        } else {
            int i;
            cin >> i;
            cout << st.sum(0, i + 1) << "\n";
        }
    }
    return 0;
}