bool is_ok(ll mid){

}

ll bisect(ll ng, ll ok){
    while(abs(ok - ng) > 1){
        ll mid = (ok + ng) / 2;
        debug(ng, mid, ok);
        if(is_ok(mid)){
            ok = mid;
        }else{
            ng = mid;
        }
    }
    return ok;
}