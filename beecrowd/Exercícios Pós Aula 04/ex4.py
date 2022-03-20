sal = float(input())
impos = 0.0

if sal <= 2000:
    print("Isento")
elif sal <= 3000.0:
    impos = (sal - 2000.0) * 0.08
    print("R$ %0.2f" %impos )
elif sal <= 4500.0:
    impos = (sal - 3000.0) * 0.18 + (1000 * 0.08)
    print("R$ %0.2f" %impos )
else:
    impos = (sal - 4500) * 0.28 + (1500 * 0.18) + (1000 * 0.08)
    print("R$ %0.2f" %impos )