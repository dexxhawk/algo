#include <bits/stdc++.h>
using namespace std;

struct segtree {
    vector<int> tree;
    int size;

    void build(vector<int>& a, int x, int lx, int rx) {
        if (rx - lx == 1) {
            if (lx < a.size() && a[lx] == 0) tree[x] = 1;
        }
        else {
            int m = (lx + rx) / 2;
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
        if (rx - lx == 1) {
            if (v) tree[x] = 0;
            else tree[x] = 1;
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

    int find(int k, int x, int lx, int rx) {
        if (rx - lx == 1){
            if (tree[x]) return lx;
            else return -2;
        } 
        int m = (lx + rx) / 2;
        if (k < tree[2 * x + 1]) {
            return find(k, 2 * x + 1, lx, m);
        } else {
            return find(k - tree[2 * x + 1], 2 * x + 2, m, rx);
        }
    }

    int find(int k) {
        return find(k, 0, 0, size);
    }
};

int main() {
    ios::sync_with_stdio(NULL), cin.tie(0), cout.tie(0);

    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    // for (int i = 0; i < n; i++) cout << a[i] << " ";
    int m;
    cin >> m;

    segtree st(a);

    while(m--) {
        char type;
        cin >> type;
        if (type == 's') {
            int k;
            cin >> k;
            k--;
            cout << st.find(k) + 1 << " ";
        } else {
            int i, v;
            cin >> i >> v;
            i--;
            st.set(i, v);
        }
    }

    return 0;
}