Ntestes = int(input())
i = 0
mensagem_final = ''
palavras = []
while i < Ntestes:
    mensagem = input()
    chave = int(input())
    for letras in mensagem:
        nova_letra = (ord(letras) - chave)
        if (nova_letra < 65):
            nova_letra = nova_letra + 26
        mensagem_final += chr(nova_letra)
    i += 1
print(palavras)

