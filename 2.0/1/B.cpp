#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int n, i, j;
    cin >> n >> i >> j;
    cout << min(abs(j - i) - 1, n - abs(j - i) - 1) << endl;
    return 0;
}