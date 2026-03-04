ca = [21,10,11,15,13]
mina = ca[0]    # 현 최솟값
minx = 0        # 현 최솟값 위치 (index)

for sb in range(1,5,1):
    if mina > ca[sb]:
        mina = ca[sb]
        minx = sb

temp = ca[0]
ca[0] = ca[minx]
ca[minx] = temp

print(ca)
# 1차목표 : [10,21,11,15,13]