#include <iostream>
using namespace std;

int INF = 1e9;
int N;
int X[150];
int Y[150];
bool seen[150];
int ans[150];

int distance(int now, int nxt){
  return (X[now] - X[nxt]) * (X[now] - X[nxt]) + (Y[now] - Y[nxt]) * (Y[now] - Y[nxt]);
}

int main(){
  cin >> N;
  for(int i = 0; i < N; i++){
    cin >> X[i] >> Y[i];
  }

  seen[0] = true;
  int now = 0;
  for(int i = 0; i < N; i++){
    ans[i] = now;
    int nxt = 0;
    int nxt_dist = INF;
    for(int j = 0; j < N; j++){
      if(seen[j] == true) continue;
      if(nxt_dist >= distance(now, j) and seen[j] == false){
        nxt = j;
        nxt_dist = distance(now, j);
      }
    }
    seen[nxt] = true;
    now = nxt;
  }
  
  for(int i = 0; i < N; i++) cout << ans[i] + 1 << endl;
  cout << 1 << endl;
}