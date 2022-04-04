i = 0
somaPares = 0
somaImpares = 0
somaPositivos = 0
somaNegativos = 0
val = 0

while i < 5:
    val = float(input())
    if val % 2 == 0:
        somaPares += 1
    else:
        somaImpares += 1
    
    if val > 0:
        somaPositivos += 1
        i += 1
    elif val == 0:
        i += 1
    else:
        somaNegativos += 1
        i += 1

print(somaPares, "valor(es) par(es)")
print(somaImpares, "valor(es) impar(es)")
print(somaPositivos, "valor(es) positivo(s)")
print(somaNegativos, "valor(es) negativo(s)")
