sal = float(input())
valRea = 0.0
newSal = 0.0

if (sal >= 0) and (sal <= 400.00):
    valRea = sal * 0.15
    newSal = sal + valRea
    print("Novo salario: %0.2f" %newSal)
    print("Reajuste ganho: %0.2f" %valRea)
    print("Em percentual: 15 %")
elif (sal >= 400.01) and (sal <= 800.00):
    valRea = sal * 0.12
    newSal = sal + valRea
    print("Novo salario: %0.2f" %newSal)
    print("Reajuste ganho: %0.2f" %valRea)
    print("Em percentual: 12 %")
elif (sal >= 800.01) and (sal <= 1200.00):
    valRea = sal * 0.10
    newSal = sal + valRea
    print("Novo salario: %0.2f" %newSal)
    print("Reajuste ganho: %0.2f" %valRea)
    print("Em percentual: 10 %")
elif (sal >= 1200.01) and (sal <= 2000.00):
    valRea = sal * 0.07
    newSal = sal + valRea
    print("Novo salario: %0.2f" %newSal)
    print("Reajuste ganho: %0.2f" %valRea)
    print("Em percentual: 7 %")
else:
    valRea = sal * 0.04
    newSal = sal + valRea
    print("Novo salario: %0.2f" %newSal)
    print("Reajuste ganho: %0.2f" %valRea)
    print("Em percentual: 4 %")
    
    


