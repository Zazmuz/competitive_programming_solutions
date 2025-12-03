#include <iostream>
#include <vector>

using namespace std;

const int MAX = 3000001;
int lp[MAX], d[MAX], cnt[MAX], omega[MAX];
vector<int> pr;

void sieve() {
    d[1] = 1;
    for (int i = 2; i < MAX; ++i) {
        if (lp[i] == 0) {
            lp[i] = i;
            pr.push_back(i);
            d[i] = 2;
            cnt[i] = 1;
            omega[i] = 1;
        }
        for (int p : pr) {
            if (p > lp[i] || i * p >= MAX) break;
            int x = i * p;
            lp[x] = p;
            if (lp[i] == p) {
                d[x] = d[i] / (cnt[i] + 1) * (cnt[i] + 2);
                cnt[x] = cnt[i] + 1;
                omega[x] = omega[i];
            } else {
                d[x] = d[i] * 2;
                cnt[x] = 1;
                omega[x] = omega[i] + 1;
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    sieve();

    int t;
    if (cin >> t) {
        while (t--) {
            int n;
            cin >> n;
            cout << d[n] - omega[n] << "\n";
        }
    }
    return 0;
}