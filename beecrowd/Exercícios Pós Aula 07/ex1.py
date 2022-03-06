# Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de 
# teste consiste de dois inteiros X e Y. Você deve apresentar a soma de todos os ímpares 
# existentes entre X e Y.

#Entrada
#A primeira linha de entrada é um inteiro N que é a quantidade de casos de teste que vem a seguir. 
# Cada caso de teste consiste em uma linha contendo dois inteiros X e Y.

#Saída
#Imprima a soma de todos valores ímpares entre X e Y.

N = int(input())
i = 0
num = 0
soma = 0
result = []
X = 0
Y = 0

while i < N:
    X, Y = input().split()
    if (int(X) > int(Y)):

        num = int(Y) + 1

        while int(num) < int(X):
            if (int(num) % 2 != 0):
                soma = int(soma) + int(num)
            num = int(num) + 1
    else:
        num = int(X) + 1
        while int(num) < int(Y):
            if (int(num) % 2 != 0):
                soma = int(soma) + int(num)
            num = int(num) + 1

    i = int(i) + 1
    result.append(soma)
    soma = 0

print("\n".join(map(str, result)))


