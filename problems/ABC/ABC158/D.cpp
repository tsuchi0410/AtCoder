#include <bits/stdc++.h>
using namespace std;
int main(){
    string S;
    cin >> S;
    int Q;
    cin >> Q;
    deque<char> dq1(S.begin(), S.end());
    S = string(S.rbegin(), S.rend());
    deque<char> dq2(S.begin(), S.end());
    bool f = false;
    int op;
    int p;
    char c;
    for (int i = 0; i < Q; i++) {
        cin >> op;
        if (op == 1) f = !f;
        if (op == 2) {
            cin >> p >> c;
            if (p == 1) {
                if (f == false) {
                dq1.push_front(c);
                dq2.push_back(c);
                } else {
                dq1.push_back(c);
                dq2.push_front(c);
                }
            } else {
                if (f == false) {
                dq1.push_back(c);
                dq2.push_front(c);
                } else {
                dq1.push_front(c);
                dq2.push_back(c);
                }
            }
        }
    }
    if (f == false) {
        for (auto &x : dq1) cout << x;
    } else {
        for (auto &x : dq2) cout << x;
    }
    cout << endl;

}