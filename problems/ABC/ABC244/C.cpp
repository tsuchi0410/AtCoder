#include <bits/stdc++.h>
using namespace std;

using ll = long long;

#define rep(i, a, b) for(int i = a; i < b; i++)
#define rrep(i, a, b) for(int i = a; i >= b; i--)
#define fore(i, a) for(auto &i : a)

#define all(x) (x).begin(),(x).end()

template <typename T>
int bisect_left(vector<T> &X, T v){
    return lower_bound(X.begin(), X.end(), v) - X.begin();
}
template <typename T>
int bisect_right(vector<T> &X, T v){
    return upper_bound(X.begin(), X.end(), v) - X.begin();
}

int main(){
    int N;
    cin >> N;
    unordered_set<int> ust;
    rep(i, 1, 2 * N + 2){
        ust.insert(i);
    }
    while(1){
        if(ust.size() > 0){
            fore(i, ust){
                cout << i << endl;
                ust.erase(i);
                break;
            }
        }
        int x;
        cin >> x;
        if(x == 0){
            return 0;
        }else{
            ust.erase(x);
        }
    }
}