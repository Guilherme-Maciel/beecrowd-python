i = 0
arr = []

while i < 100:
    arr.append(int(input()))
    i += 1

max = max(arr)
index = arr.index(max)

print(max)
print(index + 1)
