numFirst = int(input("Digite o primeiro número inteiro: "))
qtdNum = float(input("Digite a quantidade de números reais: "))
numReal = 0.0
soma = 0.0
i = 0

while i < qtdNum:
    numReal = float(input("Digite um número real: "))
    if numReal > 0:
        soma += numReal
    i += 1
    
if numFirst > 0:
    soma += numFirst

print("Soma =", soma)

