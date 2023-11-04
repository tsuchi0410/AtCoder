lambda is_ok = [&](auto&& is_ok, ll mid) -> bool{
    
};

lambda bisect = [&](auto&& bisect, ll l, ll r) -> ll{
    while(abs(r - l) > 1){
        ll mid = (r + l) / 2;
        debug(l, mid, r);
        if(is_ok(mid)){
            r = mid;
        }else{
            l = mid;
        }
    }
    return r;
};

ll l = 0;
ll r = INF;
ll ans = bisect(l, r);
