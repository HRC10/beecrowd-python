import math

Ncasas = input()
Ncasas = int(Ncasas)
cidades = []
casas = [0] * Ncasas
i = 0
while i < Ncasas:
    moradores, consumo = input().split()
    moradores = int(moradores)
    consumo = int(consumo)
    casas[i] =  (moradores, math.floor(consumo / moradores))
    
    i += 1