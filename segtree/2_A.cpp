#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

class segtree {
    public:

    struct node {
        ll seg, pref, suf, sum;
    };

    vector<node> tree;
    int size;

    const node ZERO = {0, 0, 0, 0};

    node combine(node a, node b) {
        return {
            max(a.seg, max(b.seg, a.suf + b.pref)),
            max(a.pref, a.sum + b.pref),
            max(b.suf, a.suf + b.sum),
            a.sum + b.sum,
        };
    }

    node one_element(int x) {
        return {
            max(x, 0),
            max(x, 0),
            max(x, 0),
            x
        };
    }


    void build(vector<int>& a, int x, int lx, int rx) {
        if (rx - lx == 1) {
            if (lx < a.size()) tree[x] = one_element(a[lx]);
        }
        else {
            int m = (lx + rx) / 2;
            build(a, 2 * x + 1, lx, m);
            build(a, 2 * x + 2, m, rx);
            tree[x] = combine(tree[2 * x + 1], tree[2 * x + 2]);
        }
    }

    void set(int i, int v, int x, int lx, int rx) {
        if (rx - lx == 1) {
            tree[x] = one_element(v);
            return;
        }
        int m = (lx + rx) / 2;

        if (i < m) {
            set(i, v, 2 * x + 1, lx, m);
        } else {
            set(i, v, 2 * x + 2, m, rx);
        }

        tree[x] = combine(tree[2 * x + 1], tree[2 * x + 2]);
    }


    segtree(vector<int>& a) {
        size = 1;
        while (size < a.size()) size *= 2;
        tree.assign(2 * size - 1, ZERO);
        build(a, 0, 0, size);
    }

    void set(int i, int v) {
        set(i, v, 0, 0, size);
    }


};

int main() {
    ios::sync_with_stdio(NULL);
    int n, m;
    cin >> n >> m;
    vector<int> a(n);

    for (int i = 0; i < n; i++) cin >> a[i];
    segtree st(a);
    cout << st.tree[0].seg << "\n";

    int i, v;

    while(m--) {
        cin >> i >> v;
        st.set(i, v);
        cout << st.tree[0].seg << "\n";
    }
    return 0;
}