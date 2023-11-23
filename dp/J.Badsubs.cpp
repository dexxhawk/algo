#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


int main() {
    ios::sync_with_stdio(false), cin.tie(0), cout.tie(0);
    int n;
    cin >> n;

    vector<int> dp(n + 1);
    //base
    dp[0] = 1;
    dp[1] = 3;
    // dp[i] - кол-во строк длины i, не содержащих подстроки ab
    for (int i = 2; i < n + 1; i++) {
        for (char prev : {'a', 'b', 'c'}) {
            for (char curr : {'a', 'b', 'c'}) {
                if (prev == 'a' && curr == 'b') continue;
    
            }
        } 
    }

    cout << dp[n] << "\n";
    return 0;
}