#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

struct segtree {
    vector<int> tree;
    int size;

    void build(int n, int x, int lx, int rx) {
        if (rx - lx == 1) {
            if (lx < n) tree[x] = 1;
        }
        else {
            int m = (lx + rx) / 2;
            build(n, 2 * x + 1, lx, m);
            build(n, 2 * x + 2, m, rx);
            tree[x] = tree[2 * x + 1] + tree[2 * x + 2];
        }
    }

    void build(int n) {
        size = 1;
        while(size < n) size *= 2;
        tree.assign(2 * size - 1, 0);
        
        build(n, 0, 0, size);

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

    int find(int k, int x, int lx, int rx) {
        if (rx - lx == 1) return lx;

        int m = (lx + rx) / 2;
        if (tree[2 * x + 2] > k){
            return find(k, 2 * x + 2, m, rx);
        } else {
            return find(k - tree[2 * x + 2], 2 * x + 1, lx, m);
        }
    }

    int find(int k) {
        return find(k, 0, 0, size);
    }
};


int main () {
    ios::sync_with_stdio(NULL), cin.tie(0), cout.tie(0);
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        // a[i]--;
    }

    segtree st;
    st.build(n);
    vector<int> ans(n);

    for (int i = 0; i < n; i++) {
        ans[n - i - 1] = st.find(a[n - i - 1]) + 1;
        st.set(ans[n - i - 1] - 1, 0);
    }

    for (int i = 0; i < n; i++) cout << ans[i] << " ";

    return 0;
}