S = str(input())

def bubble_sort(nlist):
    #配列の要素数num
    num = len(nlist)
    cnt = 0

    for i in range(num):
        swap = False
        for j in range(num-1, i, -1):
            #後ろから順番に隣同士の要素を比較する
            if nlist[j-1] > nlist[j]:
                nlist[j-1], nlist[j] = nlist[j], nlist[j-1]
                cnt += 1
                swap = True
        
        #交換が行われなければ終了
        if swap == False:
            break
    
    return nlist,cnt

# atcoder
num_list = []

for i in range(len(S)):
    if S[i] == 'a':
        num_list.append(0)
    if S[i] == 't':
        num_list.append(1)
    if S[i] == 'c':
        num_list.append(2)
    if S[i] == 'o':
        num_list.append(3)
    if S[i] == 'd':
        num_list.append(4)
    if S[i] == 'e':
        num_list.append(5)
    if S[i] == 'r':
        num_list.append(6)



print(bubble_sort(num_list)[1])
