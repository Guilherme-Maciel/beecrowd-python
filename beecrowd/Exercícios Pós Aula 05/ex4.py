i = 0
somaPares  = 0
val = 0

while i < 5:
    val = float(input())
    if val % 2 == 0:
        somaPares += 1
        i += 1
    else:
        i += 1

print(somaPares, "valores pares")



    