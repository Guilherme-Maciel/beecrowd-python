i = 0
soma = 0.0

while i < 2:
    n = float(input())

    if n >= 0 and n <= 10:
        soma += n
        i += 1
    else:
        print("nota invalida")

media = soma / 2
print("media = %0.2f" %media)




