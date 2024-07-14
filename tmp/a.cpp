#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int main(){
  ll D;
  cin >> D;
  vector<ll> days(D);
  for(int i = 0; i < D; i++) cin  >> days[i];
  vector<ll> ans;
  for(int i = 0; i < D - 1; i++){
    if(days[i] == 2 && days[i + 1] == 0) ans.push_back(i + 1);
  }
  if(ans.size() == 0) cout << -1 << endl;
  else{
    for(int i = 0; i < ans.size() - 1; i++){
      cout << ans[i] << " ";
    }
    cout << ans[ans.size() - 1] << endl;
  }
}