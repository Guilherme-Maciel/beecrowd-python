N = int(input("Digite o número de termos:"))
P = int(input("Digite o primeiro termo:"))
R = int(input("Digite a razão:"))
count = 0
result = []
soma = 0

result.append(P)
soma = soma + P

while count < (N - 1):
    P = P * R
    soma = soma + P
    result.append(P)
    count = count + 1

print(", ".join(map(str, result)))
print("Soma:", int(soma))



