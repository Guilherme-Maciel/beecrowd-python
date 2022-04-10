valor = int(input())
valorP = valor

ced100 = 0
ced50 = 0
ced20 = 0
ced10 = 0
ced5 = 0
ced2 = 0
ced1 = 0

ced100 = valor // 100
valor = valor - (ced100 * 100)

ced50 = valor // 50
valor = valor - (ced50 * 50)

ced20 = valor // 20
valor = valor - (ced20 * 20)

ced10 = valor // 10
valor = valor - (ced10 * 10)

ced5 = valor // 5
valor = valor - (ced5 * 5)

ced2 = valor // 2
valor = valor - (ced2 * 2)

ced1 = valor // 1
valor = valor - (ced1 * 1)

print(valorP)
print("%i nota(s) de R$ 100,00" %ced100)
print("%i nota(s) de R$ 50,00" %ced50)
print("%i nota(s) de R$ 20,00" %ced20)
print("%i nota(s) de R$ 10,00" %ced10)
print("%i nota(s) de R$ 5,00" %ced5)
print("%i nota(s) de R$ 2,00" %ced2)
print("%i nota(s) de R$ 1,00" %ced1)






