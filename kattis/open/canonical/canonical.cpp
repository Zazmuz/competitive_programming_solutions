#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<long long> coins(n);
    for (int i = 0; i < n; ++i) cin >> coins[i];
    sort(coins.begin(), coins.end());

    long long max_counter = coins[n - 1] + coins[n - 2];

    const int INF = max_counter + 10;
    vector<int> dp(max_counter + 1, INF);
    dp[0] = 0;

    for (long long cLL : coins) {
        int c = (int)cLL;
        for (int amnt = c; amnt <= max_counter; ++amnt) {
            int v = dp[amnt - c] + 1;
            if (v < dp[amnt]) dp[amnt] = v;
        }
    }

    auto greedy_count = [&](int a) -> int {
        int cnt = 0;
        long long r = a;
        while (r > 0) {
            auto it = upper_bound(coins.begin(), coins.end(), r);
            if (it == coins.begin()) return INF;
            --it;
            long long c = *it;
            cnt += (int)(r / c);
            r %= c;
        }
        return cnt;
    };

    for (int amnt = 1; amnt <= max_counter; ++amnt) {
        if (greedy_count(amnt) != dp[amnt]) {
            cout << "non-canonical\n";
            return 0;
        }
    }
    cout << "canonical\n";
    return 0;
}