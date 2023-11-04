#include <bits/stdc++.h>
using namespace std;

vector<long long> divisor(long long n) {
    vector<long long> ret;
    for (long long i = 1; i * i <= n; i++) {
        if (n % i == 0) {
            ret.push_back(i);
            if (i * i != n) ret.push_back(n / i);
        }
    }
    sort(ret.begin(), ret.end()); // 昇順に並べる
    return ret;
}

int main(){
    long long N;
    cin >> N;
    vector<long long> divisors = divisor(2 * N);
    int ans = 0;
    for (long long i = 0; i < divisors.size(); i++){
        long long n = divisors[i];
        double a = (2 * N + n - pow(n, 2.0)) / (2 * n);
        if (floor(a) == a) {
            ans++;
        }
    }
    cout << ans << endl;
}