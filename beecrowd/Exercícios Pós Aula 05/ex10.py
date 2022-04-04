N = int(input())
i = 0
qtdCobaia = 0
tipoCobaia = ""
ratos = 0
coelhos = 0
sapos = 0

while i < N:
    qtdCobaia, tipoCobaia = input().split()

    if tipoCobaia == "C":
        coelhos += int(qtdCobaia)
    elif tipoCobaia == "R":
        ratos += int(qtdCobaia)
    else:
        sapos += int(qtdCobaia)
    
    i += 1

total = ratos + coelhos + sapos

pRatos = (int(ratos)*100)/int(total)
pCoelhos = (int(coelhos)*100) / int(total)
pSapos = (int(sapos)*100)/int(total)

print("Total:",int(total), "cobaias")
print("Total de coelhos:", int(coelhos))
print("Total de ratos:", int(ratos))
print("Total de sapos:", int(sapos))
print("Percentual de coelhos: %.2f" %pCoelhos, "%")
print("Percentual de ratos: %.2f" %pRatos, "%")
print("Percentual de sapos: %.2f" %pSapos, "%")



