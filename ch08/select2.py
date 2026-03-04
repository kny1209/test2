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

print("---------------------")
# 2차목표 : [10,11,21,15,13]
mina = ca[1]  
minx = 1

for sb in range(2,5,1):
    if mina > ca[sb]:
        mina = ca[sb]
        minx = sb

temp = ca[1]
ca[1] = ca[minx]
ca[minx] = temp

print(ca)

print("---------------------")
# 3차목표 : [10,11,13,15,21]
mina = ca[2]  
minx = 2

for sb in range(3,5,1):
    if mina > ca[sb]:
        mina = ca[sb]
        minx = sb

temp = ca[2]
ca[2] = ca[minx]
ca[minx] = temp

print(ca)

print("---------------------")
# 4차목표 : [10,11,13,15,21]
mina = ca[3]  
minx = 3

for sb in range(4,5,1):
    if mina > ca[sb]:
        mina = ca[sb]
        minx = sb

temp = ca[3]
ca[3] = ca[minx]
ca[minx] = temp

print(ca)