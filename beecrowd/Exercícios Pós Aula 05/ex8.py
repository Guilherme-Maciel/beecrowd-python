N = int(input())
i = 0
result = []
val1 = 0.0
val2 = 0.0
val3 = 0.0

while i < N:
    val1, val2, val3 = input().split()
    val1 = (float(val1)*2 + float(val2)*3 + float(val3)*5) / (2 + 3 + 5)
    result.append(float(val1))
    i += 1

for x in result:
    print("%.1f" %x)