## 問題 単調減少性を利用
E - Water Tank
https://atcoder.jp/contests/abc359/tasks/abc359_e
---

### 解法
右壁が左壁より大きいならマージする。高さと横幅を管理する。

### コード
```cpp
int main(){
  LL(N);
  VEC(ll, H, N);

  stack<vector<ll>> st;
  // h, w
  // 単調減少に管理
  st.push({0, 0});
  ll ans = 1;
  rep(i, N){
    if(H[i] < st.top()[0]){
      ans += H[i];
      st.push({H[i], 1});
    }else{
      ll w = 1;
      while(!st.empty()){
        ll prev_h = st.top()[0];
        ll prev_w = st.top()[1];
        if(H[i] >= prev_h){
          w += prev_w;
          ans -= prev_h * prev_w;
        }else{
          break;
        }
        st.pop();
      }
      ans += w * H[i];
      st.push({H[i], w});
    }
    cout << ans << " ";
  }
  cout << endl;
}
```
***