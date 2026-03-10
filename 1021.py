Valor = float(input())
Centavos = int(Valor * 100)
notas100 = int(Centavos // 10000)
Centavos %= 10000
notas50 = int(Centavos // 5000)
Centavos %= 5000
notas20 = int(Centavos // 2000)
Centavos %= 2000
notas10 = int(Centavos // 1000)
Centavos %= 1000
notas5 = int(Centavos // 500)
Centavos %= 500
notas2 = int(Centavos // 200)
Centavos %= 200
Moeda1 = int(Centavos // 100)
Centavos %= 100
Moeda50 = int(Centavos // 50)
Centavos %= 50
Moeda25 = int(Centavos // 25)
Centavos %= 25
Moeda10 = int(Centavos // 10)
Centavos %= 10
Moeda05 = int(Centavos // 5)
Centavos %= 5
Moeda01 = int(Centavos // 1)
Centavos %= 1
print("NOTAS:")
print(notas100,"nota(s) de R$ 100.00")
print(notas50,"nota(s) de R$ 50.00")
print(notas20,"nota(s) de R$ 20.00")
print(notas10,"nota(s) de R$ 10.00")
print(notas5,"nota(s) de R$ 5.00")
print(notas2,"nota(s) de R$ 2.00")
print("MOEDAS:")
print(Moeda1,"moeda(s) de R$ 1.00")
print(Moeda50,"moeda(s) de R$ 0.50")
print(Moeda25,"moeda(s) de R$ 0.25")
print(Moeda10,"moeda(s) de R$ 0.10")
print(Moeda05,"moeda(s) de R$ 0.05")
print(Moeda01,"moeda(s) de R$ 0.01")



