"""
素数判定
O(√N)

ll N = 100;
bool f = isprime(N);
"""

bool isprime(long long N) {
    if (N < 2) return false;
    for (long long i = 2; i * i <= N; ++i) {
        if (N % i == 0) return false;
    }
    return true;
}