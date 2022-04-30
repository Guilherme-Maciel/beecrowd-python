i = 0
soma = 0.0
resp = 1

while resp == 1:
    while i < 2:
        n = float(input())

        if n >= 0 and n <= 10:
            soma += n
            i += 1
        else:
            print("nota invalida")

    media = soma / 2
    print("media = %0.2f" %media)
    media = 0
    soma = 0

    print("novo calculo (1-sim 2-nao)")

    resp = int(input())
    
    if resp == 1:
        i = 0

    while resp != 1 and resp != 2:
        print("novo calculo (1-sim 2-nao)")
        resp = int(input())

        if resp == 1:
            i = 0









