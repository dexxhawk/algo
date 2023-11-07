#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

    int gcd(int a, int b) {
        while (a && b){
            if (a > b) {
                a %= b;
            } else {
                b %= a;
            }
        }
        return a + b;
    }

struct segtree {
    int size;
    vector<int> tree;

    void build(vector<int>& a, int x, int lx, int rx){
        if (rx - lx == 1){
            if (lx < a.size()) tree[x] = a[lx];
        }
        else{
            int m = (lx + rx) / 2;
            build(a, 2 * x + 1, lx, m);
            build(a, 2 * x + 2, m, rx);
            tree[x] = gcd(tree[2 * x + 1], tree[2 * x + 2]);
        }
    }

    void build(vector<int>& a){
        size = 1;
        while(size < a.size()){
            size *= 2;
        }
        tree.assign(2 * size - 1, 0);
        build(a, 0, 0, size);
    }

    void set(int i, int v, int x, int lx, int rx) {
        if (rx - lx == 1) {
            tree[x] = v;
            return;
        }
        int m = (lx + rx) / 2;
        if (i < m){
            set(i, v, 2 * x + 1, lx, m);
        } else {
            set(i, v, 2 * x + 2, m, rx);
        }
        tree[x] = gcd(tree[2 * x + 1], tree[2 * x + 2]);
    }

    void set(int i, int v) {
        set(i, v, 0, 0, size);
    }

    int find_gcd(int l, int r, int x, int lx, int rx){
        if (l >= rx || lx >= r) {
            return 0;
        }
        if (lx >= l && rx <= r){
            return tree[x];
        }
        int m = (lx + rx) / 2;
        int g1 = find_gcd(l, r, 2 * x + 1, lx, m);
        int g2 = find_gcd(l, r, 2 * x + 2, m, rx);
        return gcd(g1, g2);
    }

    int find_gcd(int l, int r) {
        return find_gcd(l, r, 0, 0, size);
    }
};

int main() {
    ios::sync_with_stdio(NULL);
    int n;
    cin >> n;
    vector<int> a(n);

    for (int i = 0; i < n; i++) cin >> a[i];

    segtree st;
    st.build(a);

    int m;
    cin >> m;

    while(m--) {
        char act;
        cin >> act;

        if (act == 'g') {
            int l, r;
            cin >> l >> r;
            l--;
            cout << st.find_gcd(l, r) << "\n";
        } else {
            int i, x;
            cin >> i >> x;
            i--;
            st.set(i, x);
        }
    }


    return 0;
}