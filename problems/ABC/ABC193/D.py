from collections import defaultdict
k = int(input())
s = input()
t = input()

def setting_d():
    d = {}
    for i in range(1, 10):
        d[i] = 1 * k
    return d

def setting_d2(d, ss):   
    d2 = defaultdict(int)
    for i in ss:
        d2[int(i)] += 1
        d[int(i)] -= 1
    return d, d2

ans = 0
for s_card in range(1, 10):
    for t_card in range(1, 10):
        
        d = setting_d()

        ss = s[:4] + str(s_card)
        d, d2 = setting_d2(d, ss)

        s_score = 0
        for i in range(1, 10):
            c = 0
            if i in d2:
                c = d2[i]
            s_score += i * (10**c)

        tt = t[:4] + str(t_card)
        d, d2 = setting_d2(d, tt)

        t_score = 0
        for i in range(1, 10):
            c = 0
            if i in d2:
                c = d2[i]
            t_score += i * (10**c)
        
        # カードの枚数確認
        f = 1
        for i in d:
            if d[i] < 0:
                f = 0

        if f == 0:
            continue
        elif s_score > t_score:
            ms = k
            ms -= s.count(str(s_card))
            ms -= t.count(str(s_card))
            
            mt = k
            mt -= ss.count(str(t_card))
            mt -= t.count(str(t_card))
            
            ans += (ms / (9*k-8)) * (mt / (9*k-9))

print(ans)