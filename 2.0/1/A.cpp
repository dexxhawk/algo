#include <iostream>
using namespace std;

int main() {
    int r, i, c;
    cin >> r >> i >> c;

    int ans;

    switch (i) {
        case 0:
            ans = r ? 3 : c;
            break;
        case 1:
            ans = c;
            break;
        case 4:
            ans = r ? 3 : 4;
            break;
        case 6:
            ans = 0;
            break;
        case 7:
            ans = 1;
            break;
        default:
            ans = i;
            break;        
    }

    cout << ans << endl;

    return 0;
}