import sys

Nteste = int(sys.stdin.readline())
i = 0
while i < Nteste:
    cripto1 = ''
    Palavra = sys.stdin.readline().strip()    
    for letras in Palavra:
        if ((ord(letras) >= 65) and (ord(letras) <= 90)) or ((ord(letras) >= 97) and (ord(letras) <= 122)):
            cripto1 = cripto1 + chr(ord(letras)+3) 
        else:
            cripto1 = cripto1 + letras
    cripto2 = ''
    cripto2 = cripto1[::-1]
    cripto3 = ''
    metade = len(cripto2)//2
    cripto3 =cripto2[0:metade]
    for j in range(metade, len(cripto2)) :
        cripto3 = cripto3 + chr(ord(cripto2[j])-1)
    i += 1
    print(cripto3)
