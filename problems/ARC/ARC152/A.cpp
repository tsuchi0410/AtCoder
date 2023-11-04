#include <bits/stdc++.h>
using namespace std;

using ll = long long;

#define rep(i, a, b) for(int i = a; i < b; i++)
#define rrep(i, a, b) for(int i = a; i >= b; i--)
#define fore(i, a) for(auto &i : a)

#define all(x) (x).begin(),(x).end()

int main(){
    int N, L;
    cin >> N >> L;
    vector<int> a(N);
    unordered_map<int, int> ump;
    ump[1] = 0;
    ump[2] = 0;
    int sum = 0;
    rep(i, 0, N){
        cin >> a.at(i);
        sum += a.at(i);
        ump.at(a.at(i))++;
    }
    int cnt = 2;
    rep(i, 0, N){
        if (a.at(i) == 1){
            if (cnt > sum) break;
            else cnt += 2;
        } else {
            if (cnt > sum) break;
            else if (cnt == sum) {
                ump.at(2)--;
                break;
            } else {
                cnt += 3;
                ump.at(2)--;
            }
        }
    }
    if (ump.at(2) == 0) cout << "Yes" << endl;
    else cout << "No" << endl;
}