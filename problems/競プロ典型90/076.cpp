#include <bits/stdc++.h>
using namespace std;

using ll = long long;

#define rep(i, a, b) for(int i = a; i < b; i++)
#define rrep(i, a, b) for(int i = a; i >= b; i--)
#define fore(i, a) for(auto &i : a)

#define all(x) (x).begin(),(x).end()

int main(){
    int N;
    cin >> N;
    vector<int> A(N);
    ll sum = 0;
    rep(i, 0, N) {
        cin >> A.at(i);
        sum += A.at(i);
    }
    vector<int> v(2*N);
    rep(i, 0, N) v.at(i) = A.at(i);
    rep(i, N, 2*N) v.at(i) = A.at(i-N);
    
    queue<int> q;
    ll cnt = 0;
    fore(r, v){
        q.push(r);
        cnt += r;
        if (cnt*10 == sum) {
            cout << "Yes" << endl;
            return 0;
        }
        
        while((cnt*10 > sum) || (q.size() > N)){
            cnt -= q.front();
            q.pop();
        }
    }
    cout << "No" << endl;
}