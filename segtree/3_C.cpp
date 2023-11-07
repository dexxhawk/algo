#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

class segtree {
    int size;
    vector<int> tree;

    public:

    segtree(vector<int>& a) {
        size = 1;
        while(size < a.size()) size *= 2;
        tree.assign(2 * size - 1, 0);
    }

    void set(int i, int v, int x, int lx, int rx) {
        if (rx - lx == 1) {
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
        if (lx >= r || rx <= l) return 0;
        if (lx >= l && rx <= r) return tree[x];

        int m = (lx + rx) >> 1;
        int s1 = sum(l, r, 2 * x + 1, lx, m);
        int s2 = sum(l, r, 2 * x + 2, m, rx);
        return s1 + s2;
    }

    ll sum(int l, int r) {
        return sum(l, r, 0, 0, size);
    }
};

int main() {
    int n;
    cin >> n;
    vector<int> a(2 * n);
    vector<int> pos(n, -1);
    for (int i = 0; i < 2 * n; i++) {
        cin >> a[i];
    }
    segtree st(a);
    vector<int> ans(n);

    for (int i = 0; i < 2 * n; i++) {
        if (pos[a[i] - 1] == -1) {
            pos[a[i] - 1] = i;
        } else {
            ans[a[i] - 1] = st.sum(pos[a[i] - 1], i);
            st.set(pos[a[i] - 1], 1);
        }
    }

    for (int i = 0; i < ans.size(); i++) cout << ans[i] << " ";

    return 0;
}