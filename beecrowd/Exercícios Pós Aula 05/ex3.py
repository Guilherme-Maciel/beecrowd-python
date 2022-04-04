i = 0
qtdPositivos  = 0
somaPositivos = 0
val = 0
media = 0.0

while i < 6:
    val = float(input())
    if val != 0:
        if val > 0:
            qtdPositivos += 1
            somaPositivos += val
            i += 1
        else:
            i += 1

print(qtdPositivos, "valores positivos")
media = somaPositivos / qtdPositivos
print("%.1f" %media)