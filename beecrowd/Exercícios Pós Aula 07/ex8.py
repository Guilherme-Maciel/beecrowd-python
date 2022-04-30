n = int(input())
i = 1
loop = 1
row = 1

if 1 < n < 1000:
    while i <= (n * 2):
        if row == 1:
            if loop == 1:
                print("{} {} {}".format(row, row, row))
                loop = 2
            else:
                print("{} {} {}".format(row, row*2, row*2))
                loop = 1
                row += 1
        else:
            if loop == 1:
                print("{} {} {}".format(row, row**2, row**3))
                loop = 2
            else:
                print("{} {} {}".format(row, row**2+1, row**3+1))
                loop = 1
                row += 1
        i += 1


        