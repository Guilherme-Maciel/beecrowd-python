soma = 0
arr = []
strRes = ""

M, N = input().split()
M, N = int(M), int(N)
if N > M:
    ctrl = N
    N = M
    M = ctrl

while N > 0 and M > 0:
    while (N <= M):
        arr.append(N)
        soma += N
        N += 1
    strRes = " ".join(map(str, arr)) + " Sum={}".format(soma)
    print(strRes)
    arr.clear()
    soma = 0

    M, N = input().split()
    M, N = int(M), int(N)

    if N > M:
        ctrl = N
        N = M
        M = ctrl