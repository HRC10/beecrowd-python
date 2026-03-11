Ntestes = int(input())
i = 0
mensagem_final = ''
palavras = [0] * Ntestes
while i < Ntestes:
    mensagem = input()
    chave = int(input())
    mensagem_final = ''
    for letras in mensagem:
        nova_letra = (ord(letras) - chave)
        if (nova_letra < 65):
            nova_letra = nova_letra + 26
        mensagem_final += chr(nova_letra)
        palavras[i] = mensagem_final
    i += 1
M = 0
while M < len(palavras):
    print(palavras[M])
    M += 1
