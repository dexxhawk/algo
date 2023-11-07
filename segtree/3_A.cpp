#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

struct segtree {
    vector<ll> tree;
    int size;

    void init(int n) {
        size = 1;
        while(size < n) size *= 2;
        tree.assign(2 * size - 1, 0);
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

        tree[x] = tree[2 * x + 1] + tree[2 * x + 2];
    }

    void set(int i, int v) {
        set(i, v, 0, 0, size);
    }

    ll sum(int l, int r, int x, int lx, int rx) {
        if (l >= rx || r <= lx) {
            return 0;
        }

        if (lx >= l && rx <= r){
            return tree[x];
        }

        int m = (lx + rx) / 2;
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
    int n;
    cin >> n;
    vector<int> p(n);
    for (int i = 0; i < n; i++) {
        cin >> p[i];
        p[i]--;
    }

    segtree st;
    st.init(n);

    for (int i = 1; i < n + 1 ; i++) {
        cout << st.sum(p[i - 1] + 1, n) << " ";
        st.set(p[i], 1);
    }
    
    
    return 0;
}