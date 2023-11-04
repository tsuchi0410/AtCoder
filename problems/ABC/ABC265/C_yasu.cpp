#include<iostream>
#include<vector>
#include<map>
using namespace std;
typedef long long ll;

int main(){
    ll n, m, t;
    cin >> n >> m >> t;
    vector<ll> a(n);
    for(int i=1; i<n; i++) cin >> a.at(i);
    map<ll, ll> bonus;
    for(int i=0; i<m; i++){
        ll x, y;
        cin >> x >> y;
        bonus[x-1] = y;
    }

    bool goal = true;
    for(int i=1; i<n; i++){
        t -= a.at(i);
        if(bonus.find(i) != bonus.end()){
            t += bonus.at(i);
        }
        if(t <= 0){
            goal = false;
        }
    }
    cout << (goal ? "Yes" : "No") << endl;
}