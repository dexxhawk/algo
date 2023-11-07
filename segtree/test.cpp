#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

unordered_set<int>& foo() {
    unordered_set<int> us;
    return us;
}


int main () {
    unordered_set<int> us = foo();
    cout << us.size() << endl;

    // unordered_set<int> s1;
    // unordered_set<int> s2;
    // s1.insert(1);
    // s2.insert(2);
    // s2.insert(1);
    // s2.insert(3);

    // s1.merge(s2);
    // s1.erase(s1.begin());
    // cout << s1[0] << s1[1] << endl;
    // for(auto it = s1.begin(); it != s1.end(); it++) {
    //     cout << *it << " ";
    // }

    return 0;
}