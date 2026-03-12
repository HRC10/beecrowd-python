Nteste = int(input())
i = 0
while i < Nteste:
    k = 0
    j = 0
    voltaIndex = 0
    palavra_certaDireita = ''
    palavra_certaEsquerda = ''
    palavra_errada = input()
    teste = int(len(palavra_errada) // 2)
    while j < teste:
        palavra_certaEsquerda = palavra_certaEsquerda + palavra_errada[teste-voltaIndex-1]
        j += 1
        voltaIndex += 1
    voltaIndex = 0
    while k < teste:
        palavra_certaDireita = palavra_certaDireita + palavra_errada[len(palavra_errada)- voltaIndex-1]
        k += 1
        voltaIndex += 1
    i += 1
    print(palavra_certaEsquerda + palavra_certaDireita)