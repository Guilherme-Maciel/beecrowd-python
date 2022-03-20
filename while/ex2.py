i = 1
somaN = 0
somaP = 0

while i != 0:
    i = int(input())
    if i < 0:
        somaN += i
    else:
        somaP += i

print("Total de positivos:", somaP)
print("Total de negativos:", somaN)






