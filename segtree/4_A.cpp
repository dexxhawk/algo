#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

class segtree {
    vector<int> tree;
    int size;
    public:

    void build(vector<int>& a, int x, int lx, int rx) {
        if (rx - lx == 1) {
            if (lx < a.size()) tree[x] = a[lx];
        }
        else {
            int m = (lx + rx) >> 1;
            build(a, 2 * x + 1, lx, m);
            build(a, 2 * x + 2, m, rx);
            tree[x] = tree[2 * x + 1] + tree[2 * x + 2];
        }

    }

    segtree(vector<int>& a) {
        size = 1;
        while(size < a.size()) size *= 2;
        tree.assign(2 * size - 1, 0);
        
        build(a, 0, 0, size);
    }

    void set(int i, int v, int x, int lx, int rx) {
        if (rx - lx == 1){
            tree[x] = v;
            return;
        }

        int m = (lx + rx) >> 1;
        if (i < m) {
            set(i, v, 2 * x + 1, lx, m);
        } else {
            set(i, v, 2 * x + 2, m, rx);
        }

        tree[x] = tree[2 * x + 1] + tree[2 * x + 2];
    }

    void set(int i, int v) {
        set(i, v, 0, 0, size);
    }

    int sum(int l, int r, int x, int lx, int rx) {
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

    int sum(int l, int r) {
        return sum(l, r, 0, 0, size);
    }

};


int main () {
    ios::sync_with_stdio(NULL), cin.tie(0), cout.tie(0);
    int n, m;
    cin >> n;
    
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        if(i % 2 != 0) a[i] = -a[i];
    }
    cin >> m;

    segtree st(a);

    while(m--) {
        int type;
        cin >> type;
        if(type == 0) {
            int i, j;
            cin >> i >> j;
            i--;
            if (i % 2 != 0) j = -j;
            st.set(i, j);
        } else {
            int l, r;
            cin >> l >> r;
            l--;
            cout <<  ((l % 2 == 0) ? st.sum(l, r) : -st.sum(l, r)) << "\n";   
        }
    }
    return 0;
}