#include <bits/stdc++.h>
using namespace std;
int main(){
    int N;
    cin >> N;
    vector<long long> A(N);
    int a;
    for (int i = 0; i < N; i++) {
        cin >> a;
        A[i] = a;
    }
    vector<long long> L1, L2;
    L1.push_back(powl(10, 10));
    sort(A.begin(), A.end());
    reverse(A.begin(), A.end());
    long long ans = 0;
    bool f = true;
    for (int i = 0; i < N; i++) {
        if (i == 0) L2.push_back(A[i]);
        else if (f == true) {
            ans += min(L1[L1.size() - 1], L2[L2.size() - 1]);
            L1.push_back(A[i]);
            f = false;
        } else {
            ans += min(L1[L1.size() - 1], L2[L2.size() - 1]);
            L2.push_back(A[i]);
            f = true;
        }
    }
    cout << ans << endl;
}