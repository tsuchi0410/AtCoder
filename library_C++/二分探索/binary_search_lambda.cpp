/*

境界に関して
下限:
x か x - 1 にする

上限
現状は 1e18
オーバーフローなどに注意

*/

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


// 小数点
lambda is_ok = [&](auto&& is_ok, ld border) -> bool{

};

lambda bisect = [&](auto&& bisect, ld l, ld r) -> ld{
  while(abs(r - l) > 0.00000001){
    ld mid = (r + l) / 2;
    debug(l, mid, r);
    if(is_ok(mid)){
      r = mid;
    }else{
      l = mid;
    }
  }
  return r;
};