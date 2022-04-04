i = 0
somaPositivos  = 0
val = 0

while i < 6:
    val = float(input())
    if val != 0:
        if val > 0:
            somaPositivos += 1
            i += 1
        else:
            i += 1

print(somaPositivos, "valores positivos")



    

