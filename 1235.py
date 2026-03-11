Nteste = int(input())
i = 0
while i < Nteste:
    palavra_errada = input()
    teste = int(len(palavra_errada) / 2)
    palavra_certa = palavra_errada[teste]
    print(palavra_errada[teste])
    i += 1