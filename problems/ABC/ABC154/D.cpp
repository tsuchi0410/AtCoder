#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, K;
    cin >> N >> K;
    
    vector<int> p(N);
    for (int i = 0; i < N; i++) {
        cin >> p[i];
    }
    
    vector<double> v(1001, 0);
    for (int i = 1; i <= 1000; i++) {
        double a = 0;
        for (int j = 0; j < i; j++) {
            a += (j + 1) * (1.0 / i);
        }
        v[i] = a;
    }
    
    double ans = 0;
    double a = 0;
    int r = 0;
    for (int l = 0; l < N; l++) {
        a += v[p[l]];
        
        if (l - r + 1 < K) {
            continue;
        }
        
        if (l - r + 1 > K) {
            a -= v[p[r]];
            r++;
        }
        
        if (l - r + 1 == K) {
            ans = max(ans, a);
        }
    }
    
    cout << setprecision(7) << ans << endl;
}
