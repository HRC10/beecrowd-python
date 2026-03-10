horaInicial, minutoInicial, horaFinal, minutoFinal = input().split()
horaInicial = int(horaInicial)
minutoInicial = int(minutoInicial)
horaFinal = int(horaFinal)
minutoFinal= int(minutoFinal)
hora = int()
minuto = int()
FimMinutos = (horaFinal * 60)+ minutoFinal
InicioMinutos = (horaInicial * 60) + minutoInicial
if (InicioMinutos >= FimMinutos):
    hora = ((1440-InicioMinutos)+FimMinutos) // 60
    minuto = ((1440-InicioMinutos)+FimMinutos) % 60
    print("O JOGO DUROU",hora,"HORA(S) E",minuto,"MINUTO(S)")

else:
    hora = (FimMinutos - InicioMinutos) // 60
    minuto = (FimMinutos - InicioMinutos) % 60
    print("O JOGO DUROU",hora,"HORA(S) E",minuto,"MINUTO(S)")
