aba, n_acoes = input().split()
aba = int(aba)
acoes = int(n_acoes)
for i in range(acoes):
    acoes = input()
    if (acoes == 'fechou'):
        aba += 1
    else:
        aba -= 1
print(aba)    

