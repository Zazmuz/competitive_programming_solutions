#include <iostream>
#include <vector>
#include <cmath>
#include <cstdlib>

using namespace std;

void solve() {
    long long n;
    cin >> n;

    if (n < 2) {
        cout << 0 << endl;
        exit(0);
    }

    long long s = sqrt(n);
    vector<long long> vals;
    long long i = 1;

    while (i <= n) {
        long long v = n / i;
        i = n / v + 1;
        vals.push_back(v);
    }

    int m = vals.size();
    vector<int> id1(s + 1);
    vector<int> id2(s + 1);

    for (int i = 0; i < m; ++i) {
        long long v = vals[i];
        if (v <= s) {
            id1[v] = i;
        } else {
            id2[n / v] = i;
        }
    }

    vector<long long> g;
    g.reserve(m);
    for (long long v : vals) {
        g.push_back(v - 1);
    }

    for (int p = 2; p <= s; ++p) {
        if (g[id1[p]] == g[id1[p - 1]]) {
            continue;
        }

        long long sp = g[id1[p - 1]];
        long long p2 = (long long)p * p;

        for (int i = 0; i < m; ++i) {
            long long v = vals[i];
            if (v < p2) break;

            long long div = v / p;
            int idx = (div <= s) ? id1[div] : id2[n / div];
            g[i] -= g[idx] - sp;
        }
    }

    cout << g[0] << endl;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    solve();
    return 0;
}