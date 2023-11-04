from itertools import*
s = "122334445"
l = [[k,len(list(v))] for k,v in groupby(s)]
#l = [len(list(v)) for k,v in groupby(s)]
print(l)

# 復元
r = []
for i in l:
    buf = i[0] * i[1]
    r.append(buf)
print("".join(r))