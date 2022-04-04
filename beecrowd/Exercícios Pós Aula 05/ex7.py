N = int(input())
X = 0
inside = 0
outside = 0
val = 0

while X < N:
    val = int(input())

    if val >= 10 and val <= 20:
        inside += 1
    else:
        outside += 1

    X += 1

print(inside, "in")
print(outside, "out")