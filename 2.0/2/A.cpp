#include <iostream>
using namespace std;

int main() {
    int x = 0, mxm = 0, ans = 0;
    while(true) {
        cin >> x;
        if (x == 0) break;
        if (x == mxm) ans++;
        else if (x > mxm) {
            ans = 1;
            mxm = x;
        }
    }

    cout << ans << endl;

    return 0;
}