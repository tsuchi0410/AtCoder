#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int main(){
  ll N, K;
  cin >> N >> K;
  vector<ll> A(N);
  for(int i = 0; i < N; i++){
    cin >> A[i];
  }

  set<ll> st;
  st.insert(0);
  for(int i = 0; i < K; i++){
    for(int j = 0; j < N; j++){
      st.insert(*st.begin() + A[j]);
    }
    st.erase(*st.begin());
  }

  cout << *st.begin() << endl;

}