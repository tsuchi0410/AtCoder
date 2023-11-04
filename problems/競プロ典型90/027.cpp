#include <iostream>
#include <string>
#include <algorithm>
#include <map>
#include <vector>

#define rep(i, n) for (int i = 0; i < n; i++)
#define append push_back

using namespace std;

int main(){

    int n;
    string s;
    
    cin >> n;

    map<string, int> l;
    vector<int> v;
    rep(i, n){
        cin >> s;
        l[s] += 1;

        if (l[s] == 1){
            v.append(i+1);
        }
    }

    n = v.size();
    rep(i, n) cout << v[i] << endl;


}