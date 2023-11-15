/*

初項 = a
末項 = b
項数 = n

とすると、
(a + b) * n / 2

引数 (初項、項数)
ll ans = sum_of_sequences(a, n);

*/

long long sum_of_sequences(long long a, long long n){
  return (a + a * n) * n / 2;
}