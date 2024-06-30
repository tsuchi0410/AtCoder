#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int INF = 1e9;
int N;
int X[150];
int Y[150];
int P[151];
int NMAX = 2e5;

// a 以上 b 以下の整数
int get_random_int(int a, int b){
  return a + rand() % (b - a + 1);
}

// 0 以上 1 以下のランダムな実数を返す変数
double get_random_double(){
  return 1.0 * rand() / RAND_MAX;
}

double calc_score(int now, int nxt){
  return sqrt((X[now] - X[nxt]) * (X[now] - X[nxt]) + (Y[now] - Y[nxt]) * (Y[now] - Y[nxt]));
}

double get_score(int *P){
  double score = 0;
  for(int i = 0; i < N; i++) score += calc_score(P[i], P[i + 1]);
  return score;
}

int main(){
  cin >> N;
  for(int i = 0; i < N; i++){
    cin >> X[i] >> Y[i];
  }

  // 初期解生成
  for(int i = 0; i < N; i++) P[i] = i;

  double current_score = get_score(P);
  for(int i = 0; i < NMAX; i++){
    int left = get_random_int(1, N - 1);
    int right = get_random_int(1, N - 1);
    if(right < left) swap(right, left);
    reverse(P + left, P + right + 1);
    double new_score = get_score(P);

    double T = 30.00 - 28.00 * (i + 1) / (double)NMAX;
    double probability = exp(min(0.0, (current_score - new_score) / T));
    if(get_random_double() < probability){
      current_score = new_score;
    }else{
      reverse(P + left, P + right + 1);
    }
  }
  
  for(int i = 0; i < N; i++) cout << P[i] + 1 << endl;
  cout << 1 << endl;
}