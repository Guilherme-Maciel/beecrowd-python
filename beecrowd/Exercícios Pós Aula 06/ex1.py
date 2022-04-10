v1, v2, v3 = input().split()
v1, v2, v3 = int(v1), int(v2), int(v3)

maior = (v1 + v2 + abs(v1 - v2)) / 2
maior = (int(maior) + v3 + abs(int(maior) - v3)) / 2

print("%d eh o maior" %maior)
