M, N = input().split()
M, N = int(M), int(N)

while N != M:
    if N > M:
        msg = "Crescente"
    else:
        msg = "Decrescente"
    print(msg)
    M, N = input().split()
    M, N = int(M), int(N)