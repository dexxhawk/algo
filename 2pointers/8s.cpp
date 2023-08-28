#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int n;
ll c, cnta, cntb, rdn;
string s;

void add (char ch) {
    if (ch == 'a') cnta++;
    else if (ch == 'b') cntb++, rdn += cnta;
}

bool good () {
    return rdn <= c;
}

void remove (char ch) {
    if (ch == 'a') cnta--, rdn -= cntb;
    else if (ch == 'b') cntb--;
}


int main() {
    ios::sync_with_stdio(false);

    cin >> n >> c;
    cin >> s;

    ll l = 0;
    ll res = 0;

    for (int r = 0; r < n; r++) {
        add(s[r]);
        while (!good()) {
            remove(s[l]);
            l++;
        }

        res = max(res, r - l + 1);
    }


    cout << res;


    return 0;
}


