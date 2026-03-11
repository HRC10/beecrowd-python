
Ntestes = input()
Ntestes = int(Ntestes)
casas = [] * Ntestes
i = 0
media = [0] * Ntestes
while i < Ntestes:
    Moradores, Consumo = map(int, input().split())
    media[i] = (Moradores, (Consumo // Moradores))
    i += 1
media.sort()
print(media)
