X = int(input())
Y = int(input())
soma = 0

if Y > X:
    X = Y
    Y = X

Y += 1

while Y < X:
    if Y % 2 != 0:
        soma += Y
    Y += 1

print(soma)

