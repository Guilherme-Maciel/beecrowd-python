seg = int(input())
min = 0
hor = 0

min = seg // 60
seg = seg - (min * 60)

hor = min // 60
min = min - (hor * 60)

print("%d:%d:%d" % (hor, min, seg))