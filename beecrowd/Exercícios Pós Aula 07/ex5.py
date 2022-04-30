X, Y = input().split()
X, Y = int(X), int(Y)

while X != 0 and Y != 0:
    
    if X > 0 and Y > 0:
        print("primeiro")
    if X < 0 and Y > 0:
        print("segundo")
    if X < 0 and Y < 0:
        print("terceiro")
    if X > 0 and Y < 0:
        print("quarto")
    X, Y = input().split()
    X, Y = int(X), int(Y)



    
