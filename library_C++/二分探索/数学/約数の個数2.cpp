"""
ll ans = number_of_divisors(N);
O(√N)
"""


long long number_of_divisors(long long n){
    if (n==0){
        return 0;
    }else{
        long long i=2;
        long long num=1;
        long long cnt=1;
        long long f=0;
        while (i*i<=n){
            cnt=1;
            f=0;
            while (n%i==0){
                n/=i;
                cnt++;
                f=1;
            }
            i++;
            if (f){
                num*=cnt;
            }
        }
        if (n>1){
            num*=2;
        }
        return num;
    }
}

