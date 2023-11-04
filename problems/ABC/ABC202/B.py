S = input()

S = S[::-1]

S = S.replace('6', 'a')
S = S.replace('9', '6')
S = S.replace('a','9')

print(S)
