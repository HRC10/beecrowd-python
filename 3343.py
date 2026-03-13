import sys
input = sys.stdin.readline

Ntitas, tamanhoMuralha = map(int, input().split())
Titas = input()
P, M, G = map(int, input().split())
Muros = 0
Muralha = tamanhoMuralha
Muros = 1
for ataque in Titas:
    if ataque == 'P':
        if Muralha - P >= P or Muralha - P == 0:
            Muralha = Muralha - P
            print("atacou, VIDA", Muralha)
        elif Muralha == 0 or Muralha - P < P:
            print("Pulou VIDA", Muralha)
            Muros += 1
            Muralha = tamanhoMuralha
            print(Muros, "MURO NOVO")
print(Muros)